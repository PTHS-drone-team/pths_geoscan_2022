local boardNumber = boardNumber
local unpack = table.unpack
local points = {
{-0.8660254037844384, -0.5000000000000004, 0},
{-0.9659258262890681, -0.2588190451025215, 0},
{-1.0, -1.8369701987210297e-16, 0},
{-0.9659258262890684, 0.2588190451025203, 0},
{-0.866025403784439, 0.49999999999999933, 0},
{-0.7071067811865483, 0.7071067811865468, 0},
{-0.5000000000000004, 0.8660254037844384, 0},
{-0.25881904510252157, 0.9659258262890681, 0},
{-2.4492935982947064e-16, 1.0, 0},
{0.25881904510252024, 0.9659258262890684, 0},
{0.4999999999999993, 0.866025403784439, 0},
{0.7071067811865474, 0.7071067811865477, 0},
{0.8660254037844388, 0.4999999999999997, 0},
{0.9659258262890683, 0.25881904510252074, 0},
{1.0, 3.061616997868383e-16, 0},
{0.9659258262890684, -0.2588190451025202, 0},
{0.8660254037844383, -0.5000000000000008, 0},
{0.7071067811865485, -0.7071067811865467, 0},
{0.4999999999999998, -0.8660254037844388, 0},
{0.2588190451025225, -0.9659258262890679, 0},

}

local curr_point = 1

local function nextPoint()
    if(#points >= curr_point) then
        ap.goToLocalPoint(unpack(points[curr_point]))
        curr_point = curr_point + 1
    else
        ap.push(Ev.MCE_LANDING)
    end
end

function callback(event)
    if(event == Ev.POINT_REACHED) then
        nextPoint()
    end
end
nextPoint()