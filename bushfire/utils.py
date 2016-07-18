from bushfire.models import (Bushfire)

def breadcrumbs_li(links):
    """Returns HTML: an unordered list of URLs (no surrounding <ul> tags).
    ``links`` should be a iterable of tuples (URL, text).
    """
    crumbs = ''
    li_str = '<li><a href="{}">{}</a></li>'
    li_str_last = '<li class="active"><span>{}</span></li>'
    # Iterate over the list, except for the last item.
    if len(links) > 1:
        for i in links[:-1]:
            crumbs += li_str.format(i[0], i[1])
    # Add the last item.
    crumbs += li_str_last.format(links[-1][1])
    return crumbs


def calc_coords(obj):
        coord_type = obj.coord_type
        if coord_type == Bushfire.COORD_TYPE_MGAZONE:
            obj.lat_decimal = float(obj.mga_zone)/2.0
            obj.lat_degrees = float(obj.mga_zone)/2.0
            obj.lat_minutes = float(obj.mga_zone)/2.0

            obj.lon_decimal = float(obj.mga_zone)/2.0
            obj.lon_degrees = float(obj.mga_zone)/2.0
            obj.lon_minutes = float(obj.mga_zone)/2.0

        elif coord_type == Bushfire.COORD_TYPE_LATLONG:
            obj.mga_zone = float(obj.lat_decimal) * 2.0
            obj.mga_easting = float(obj.lat_decimal) * 2.0
            obj.mga_northing = float(obj.lat_decimal) * 2.0


