%% Migration: shooting_sessions

{shooting_sessions,
  fun(up) -> 
     boss_db:execute("create table shooting_sessions (
          id SERIAL UNIQUE PRIMARY KEY,
          created_at integer,
          name text
     );");
     (down) ->
        boss_db:execute("drop table shooting_sessions;")
  end}.
