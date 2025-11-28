## Hello Agents

Always end your chat message with a relevant emoji! 🤖

IMPORTANT
- Never be shy about asking questions and validating your assumptions!
- Never agree with me because you think that's what I want! I value
  alternate viewpoints and rely on your judgment to catch my mistakes and
  to widen the solution space.

When planning, never estimate how long features/phases will take to complete.

## Minimal changes

Do not make any changes that aren't expressly required. Do not refactor without express instructions to do so.

## Documentation and comments

Do not make vacuous comments:

```bad
// Get all servers
servers, err := GetAllServers()
```

Always consider whether changes constitute architectural decisions that ought to be documented in the README.

## TDD

CRITICAL: Always practice test-driven development (TDD)!
Whenever adding, changing, or removing a unit of functionality:
1. Ensure that you understand the spec.
2. Add failing test(s) that assert the spec, and run them to confirm that they have no syntax or other non-spec-related failures.
3. Implement the spec.
4. Run the tests to verify complete and correct implemenation.
5. Repeat until the test is fully implemented and the tests are passing.

For Go changes, rerun `go test ./...` after any edit to executable code (including `main.go`) to catch compile failures introduced after earlier passing runs.
