-module(shooting_ground_index_controller, [Req]).
-compile(export_all).

index('GET', []) ->
 ShootingSessions = boss_db:find(shooting_session, []),
 {ok, [{shooting_sessions, ShootingSessions}]}.
