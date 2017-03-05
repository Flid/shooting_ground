-module(shooting_ground_custom_filters).
-compile(export_all).

% put custom filters in here, e.g.
%
% my_reverse(Value) ->
%     lists:reverse(binary_to_list(Value)).
%
% "foo"|my_reverse   => "oof"


format_unixtime(Value) ->
  {Days, {H, M, S}} = calendar:seconds_to_daystime(Value),
  {Year, Month, Day} = calendar:gregorian_days_to_date(Days),
  io_lib:format("~4..0w/~2..0w/~2..0w ~2..0w:~2..0w:~2..0w", [
    Year + 1970, Month, Day,
    H, M, S
  ]).


get_id(Value) ->
  lists:last(string:tokens(Value, "-")).
