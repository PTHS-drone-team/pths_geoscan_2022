local boardNumber = boardNumber
local unpack = table.unpack
local points = {
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},
{0, 0, 1},

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
