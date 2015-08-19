from bottle import get, route, request, response, run, post
import somelib


def handle_padded(handler):
    def decorator(**kwargs):
        r = handler(kwargs)
        try:
            callback = request.query.get('callback')
        except Exception, e:
            callback = None
        if callback is None:
            return r
        else:
            response.content_type = 'text/javascript'
            return "%s(%r);" % (callback, r)
    return decorator


@get('/mouse/<cheese>/<trap>/<cat>')
@handle_padded
def mouse(kargs):
    r = {'return_value': somelib.mouse(int(kargs['cheese']), int(kargs['trap']), int(kargs['cat']))}
    return r


@get('/dog/<bone>')
@handle_padded
def dog(kargs):
    r = {'return_value': somelib.dog(int(kargs['bone']))}
    return r


run(host='0.0.0.0', port=8080, debug=True)
