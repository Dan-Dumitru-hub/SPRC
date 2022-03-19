from copy import deepcopy

from flask import Flask, request, jsonify, Response, json

app = Flask(__name__)
countries = []
cities = []
next_country = 1
next_city = 1
temperatures=[]
next_temperature=1


@app.route("/api/countries", methods=["POST"])
def postcountrie():
    global countries
    global next_country
    params = request.get_json(silent=True)
    if not params:
        return Response(status=400)

    if params.get('nume') is None:
        return Response(status=400)
    if params.get('lat') is None:
        return Response(status=400)
    if params.get('lon') is None:
        return Response(status=400)

    new_entry = {'id': next_country,
                 'nume': params['nume'],
                 'lat': params['lat'],
                 'lon': params['lon']}
    next_country += 1


    countries.append(new_entry)
    str = {'id': next_country - 1}


    return jsonify(str), 201


@app.route("/api/countries", methods=["GET"])
def getcountry():
    global countries
    return jsonify(countries)


@app.route("/api/countries/<ID>", methods=["PUT"])
def putcountry(ID):
    global countries
    #print(countries)

    for i in range(0, len(countries) ):
        if countries[i]['id'] == int(ID):
            params = request.get_json(silent=True)
            if not params:
                return Response(status=400)

            if params.get('nume') is None:
                return Response(status=400)
            if params.get('lat') is None:
                return Response(status=400)
            if params.get('lon') is None:
                return Response(status=400)

            countries[i]['nume'] = params['nume']
            countries[i]['lat'] = params['lat']
            countries[i]['lon'] = params['lon']

            return Response(status=200)

    return Response(status=400)


@app.route("/api/countries/<ID>", methods=["DELETE"])
def deletcountry(ID):
    global countries
    #print(countries)

    for i in range(0, len(countries) ):
        if countries[i]['id'] == int(ID):
            res = [i for i in countries if not (i['id'] == int(ID))]

            countries = deepcopy(res)

            return Response(status=200)

    return Response(status=404)


@app.route("/api/cities", methods=["POST"])
def post_cities():
    global cities
    global next_city
    global countries
    #print(countries)
    params = request.get_json(silent=True)
    if not params:
        return Response(status=400)

    if params.get('nume') is None:
        return Response(status=400)
    if params.get('lat') is None:
        return Response(status=400)
    if params.get('lon') is None:
        return Response(status=400)
    if params.get('idTara') is None:
        return Response(status=400)
    ok=1
    for i in range(0, len(countries)):
        if countries[i]['id'] == params.get('idTara'):
            ok=0

    if ok ==1:
        return Response(status=400)

    new_entry = {'idTara': params['idTara'],
                 'id': next_city,
                 'nume': params['nume'],
                 'lat': params['lat'],
                 'lon': params['lon']
                 }
    next_city += 1


    cities.append(new_entry)
    str = {'id': next_city - 1}


    return jsonify(str), 201


@app.route("/api/cities", methods=["GET"])
def getcity1():
    global cities
    return jsonify(cities)


@app.route("/api/cities/country/<ID>", methods=["GET"])
def getcity2(ID):
    global cities
    #print(int(ID) in cities[0])
    #print(" id" + str(int(ID)))
    list =[]

    for i in range(len(cities) ):
        if cities[i]['idTara'] == int(ID):
            list.append(cities[i])
    return jsonify(list)




@app.route("/api/cities/<ID>", methods=["PUT"])
def putcities(ID):
    global cities
    global countries
    #print(cities)

    for i in range(0, len(cities) ):
        if cities[i]['id'] == int(ID):
            params = request.get_json(silent=True)
            if not params:
                return Response(status=400)

            if params.get('nume') is None:
                return Response(status=400)
            if params.get('lat') is None:
                return Response(status=400)
            if params.get('lon') is None:
                return Response(status=400)
            if params.get('idTara') is None:
                return Response(status=400)

            ok = 1
            for j in range(0, len(countries)):
                if countries[j]['id'] == params.get('idTara'):
                    ok = 0

            if ok == 1:
                return Response(status=400)

            cities[i]['nume'] = params['nume']
            cities[i]['lat'] = params['lat']
            cities[i]['lon'] = params['lon']
            cities[i]['idTara'] = params['idTara']

            return Response(status=200)

    return Response(status=400)


@app.route("/api/cities/<ID>", methods=["DELETE"])
def deletecity(ID):
    global cities
    #print(cities)

    for i in range(0, len(cities)):
        if cities[i]['id'] == int(ID):
            res = [i for i in cities if not (i['id'] == int(ID))]

            cities = deepcopy(res)

            return Response(status=200)

    return Response(status=404)




@app.route("/api/temperatures", methods=["POST"])
def posttemp():
    global temperatures
    global next_temperature
    global cities
    #print(cities)
    params = request.get_json(silent=True)
    if not params:
        return Response(status=400)

    if params.get('idOras') is None:
        return Response(status=400)
    if params.get('valoare') is None:
        return Response(status=400)
    ok = 1
    for i in range(0, len(cities) ):

        if cities[i]['id'] == params.get('idOras'):
            ok = 0

    if ok == 1:
        return Response(status=400)


    new_entry = {'id': next_temperature,
                 'idOras': params['idOras'],
                 'valoare': params['valoare'],
                 }
    next_temperature += 1


    temperatures.append(new_entry)
    str = {'id': next_temperature - 1}


    return jsonify(str), 201



@app.route("/api/temperatures/<ID>", methods=["PUT"])
def puttemp(ID):
    global temperatures
    global  cities
    #print(temperatures)

    for i in range(0, len(temperatures) ):
        if temperatures[i]['id'] == int(ID):
            params = request.get_json(silent=True)
            if not params:
                return Response(status=400)

            if params.get('idOras') is None:
                return Response(status=400)
            if params.get('valoare') is None:
                return Response(status=400)
            ok = 1
            for j in range(0, len(cities)):

                if cities[j]['id'] == params.get('idOras'):
                    ok = 0

            if ok == 1:
                return Response(status=400)


            temperatures[i]['idOras'] = params['idOras']
            temperatures[i]['valoare'] = params['valoare']


            return Response(status=200)

    return Response(status=400)


@app.route("/api/temperatures/<ID>", methods=["DELETE"])
def deletetemp(ID):
    global temperatures
    #print(temperatures)

    for i in range(0, len(temperatures) ):
        if temperatures[i]['id'] == int(ID):
            res = [i for i in temperatures if not (i['id'] == int(ID))]

            temperatures = deepcopy(res)

            return Response(status=200)

    return Response(status=404)

@app.route("/reset", methods=["DELETE"])
def deletall():
    global countries
    global next_country
    #print(countries)

    countries = []
    next_country = 1

    return Response(status=200)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
