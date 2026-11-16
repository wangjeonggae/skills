# Issue tracker: GitHub

Issues and specs live in https://github.com/wangjeonggae/skills/issues.
Use GitHub tools or the authenticated gh CLI.
Always explicitly target wangjeonggae/skills; never the upstream repository.

Publishing a spec or ticket means creating a GitHub issue.
Read the relevant issue, labels, and comments before acting.
Use native sub-issues and blocking dependencies when supported.
Otherwise record Part of #<parent> and Blocked by: #<blocker>
in the issue body. Work is unblocked when all blockers are closed.
Explain a resolution before closing an issue.

## Pull requests as a triage surface
PRs as a request surface: no.

## Wayfinding
Keep the map in one issue labelled wayfinder:map.
Link child tickets as sub-issues, or use a task list in the map.
Use wayfinder:research, wayfinder:prototype, wayfinder:grilling,
or wayfinder:task for child types.
Choose an unassigned child with no open blockers in map order.
Assign it when claiming; record its outcome in the map on resolution.
