local boardNumber = boardNumber
local unpack = table.unpack
local points = {
{0.8660254037844387, -0.49999999999999983, 0},
{0.7071067811865476, -0.7071067811865475, 0},
{0.5000000000000003, -0.8660254037844385, 0},
{0.258819045102521, -0.9659258262890682, 0},
{1.2246467991473532e-16, -1.0, 0},
{-0.25881904510252035, -0.9659258262890684, 0},
{-0.4999999999999994, -0.866025403784439, 0},
{-0.7071067811865471, -0.7071067811865479, 0},
{-0.8660254037844384, -0.5000000000000004, 0},
{-0.9659258262890683, -0.25881904510252063, 0},
{-1.0, -1.8369701987210297e-16, 0},
{-0.9659258262890684, 0.2588190451025203, 0},
{-0.8660254037844386, 0.5000000000000001, 0},
{-0.707106781186547, 0.707106781186548, 0},
{-0.49999999999999967, 0.8660254037844388, 0},
{-0.2588190451025207, 0.9659258262890683, 0},
{-2.4492935982947064e-16, 1.0, 0},
{0.25881904510252024, 0.9659258262890684, 0},
{0.4999999999999993, 0.866025403784439, 0},
{0.7071067811865467, 0.7071067811865483, 0},

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
