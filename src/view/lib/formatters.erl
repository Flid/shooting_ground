-module(formatters).
-compile(export_all).

format_shooting_session(Session) ->
  [
    {id, Session:id()},
    {created_at, Session:created_at()},
    {name, Session:name()}
  ].
