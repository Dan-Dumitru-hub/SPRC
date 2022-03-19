from copy import deepcopy

from flask import Flask, request, jsonify,Response


app = Flask(__name__)
movies=[]
next_movie=1

@app.route("/movies", methods=["POST"])
def post_movie():
    global movies
    global next_movie
    params= request.get_json(silent=True)
    if not params:
        return Response(status=400)

    if params.get('nume') is None:
        return Response(status=400)

    new_movie={'id':next_movie,
               'nume':params['nume']}
    next_movie += 1
    movies.append(new_movie)


    return Response(status=201)

@app.route("/movies",methods=["GET"])
def getmovies():
    global movies
    return jsonify(movies)

@app.route("/movie/<ID>",methods=["GET"])
def getmovie(ID):
    global movies
    print(int(ID) in movies[0] )
    print( " id"+ str(int(ID)))


    for i in range(0,len(movies)-1):
       if  movies[i]['id'] == int(ID) :

            return jsonify(movies[i])

    return Response(status=404)

@app.route("/movie/<ID>",methods=["PUT"])
def putmovie(ID):
    global movies
    print(movies)

    for i in range(0, len(movies) - 1):
        if movies[i]['id'] == int(ID):
            params = request.get_json(silent=True)
            if not params:
                return Response(status=400)

            if params.get('nume') is None:
                return Response(status=400)

            new_movie = {'id': int(ID),
                         'nume': params['nume']}
            movies[i]['nume'] = params['nume']


            return Response(status=200)


    return Response(status=400)



@app.route("/movie/<ID>",methods=["DELETE"])
def deletmovie(ID):
    global movies
    print(movies)

    for i in range(0, len(movies) - 1):
        if movies[i]['id'] == int(ID):
            res = [i for i in movies if not (i['id'] == int(ID))]
            'del movies[i]'
            movies=deepcopy(res)


            return Response(status=200)


    return Response(status=404)



@app.route("/reset",methods=["DELETE"])
def deletall():
    global movies
    global next_movie
    print(movies)

    movies = []
    next_movie = 1

    return Response(status=200)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

