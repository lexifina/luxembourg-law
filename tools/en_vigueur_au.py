"""Prints an act, or one article of it, as it stood on a given day, from this repository's history.

    python tools/en_vigueur_au.py 2021-06-01 constitution art_32     # Art. 32 of the Constitution on 1 June 2021
    python tools/en_vigueur_au.py 1950-01-01 constitution            # the whole Constitution on 1 January 1950
    python tools/en_vigueur_au.py 2021-03-01 covid art_3bis          # the Covid-19 law

The act can be named by its folder (constitution/1868/10/17/n1, loi/2020/07/17/a624) or by "constitution" / "covid".
Every commit carries the day its text applies from in its "In-force:" trailer. Commits before 1970 are dated
1970-01-01 because git cannot store older dates, so the day is read from the trailer, never from the commit date.
"""
import datetime as dt
import subprocess
import sys

ALIASES = {'constitution': 'constitution/1868/10/17/n1', 'covid': 'loi/2020/07/17/a624', 'loi-covid-19': 'loi/2020/07/17/a624'}


def git(*args: str, cwd=None) -> str:
    return subprocess.run(['git', *args], capture_output=True, text=True, encoding='utf-8', check=True, cwd=cwd).stdout


def commit_on(day: str, path: str, cwd=None, branch: str = 'main') -> str | None:
    """The last commit touching `path` whose In-force day is on or before `day` (history is linear and in order)."""
    out = git('log', '--format=%H%x00%(trailers:key=In-force,valueonly,separator=)%x01', branch, '--', path, cwd=cwd)
    for rec in out.split('\x01'):
        rec = rec.strip()
        if not rec:
            continue
        h, d = rec.split('\x00')
        if d.strip() and d.strip() <= day:
            return h
    return None


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    day, act = sys.argv[1], ALIASES.get(sys.argv[2], sys.argv[2]).strip('/')
    dt.date.fromisoformat(day)
    branch = 'futur' if day > dt.date.today().isoformat() and git('branch', '--list', 'futur').strip() else 'main'
    commit = commit_on(day, act, branch=branch)
    if not commit:
        sys.exit(f'{act} is not in the record on {day}.')
    if len(sys.argv) > 3:
        try:
            print(git('show', f'{commit}:{act}/{sys.argv[3]}.md'), end='')
        except subprocess.CalledProcessError:
            sys.exit(f'{sys.argv[3]} was not in force on {day}.')
        return
    for f in git('ls-tree', '--name-only', commit, f'{act}/').split():
        if f.endswith('.md') and not f.endswith('README.md'):
            print(git('show', f'{commit}:{f}'))


if __name__ == '__main__':
    main()
