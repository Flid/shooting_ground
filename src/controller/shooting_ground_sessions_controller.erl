-module(shooting_ground_sessions_controller, [Req]).
-compile(export_all).

create('POST', []) ->
  Time = round(os:system_time() / 1000000000),
  Name = Req:post_param("name"),
  Session = shooting_session:new(id, Time, Name),
  {ok, SavedSession} = Session:save(),
  {json, [
    {status, "ok"},
    {shooting_session, [
      {id, SavedSession:id()},
      {created_at, SavedSession:created_at()},
      {name, SavedSession:name()}
    ]
    }
  ]}.


list('GET', []) ->
  {json, [{status, "ok"}]}.



create_item('POST', []) ->
  SessionId = list_to_integer(Req:post_param("session_id")),
  Seconds = list_to_integer(Req:post_param("seconds")),
  Data = Req:post_param("data"),
  io:format("sssss ~w~n", [SessionId]),


  SessionItem = shooting_session_item:new(id, SessionId, Seconds, Data),
  {ok, SavedSessionItem} = SessionItem:save(),
  {json, [{status, "ok"}]}.
