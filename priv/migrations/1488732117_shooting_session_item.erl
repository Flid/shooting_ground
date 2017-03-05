%% Migration: shooting_session_item

{shooting_session_item,
  fun(up) ->
      boss_db:execute("create table shooting_session_items (
          id SERIAL UNIQUE PRIMARY KEY,
          session_id integer references shooting_sessions (id),
          seconds integer,
          data text
     );");
     (down) ->
        boss_db:execute("drop table shooting_session_items;")
  end}.
