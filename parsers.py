from flask_restx.reqparse import RequestParser

"""def get_arguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument("person_id", default=None)
        parser.add_argument("comment", default="")
        parser.add_argument("name", default="main")
        parser.add_argument("revision", default=1, type=int)
        parser.add_argument("change_status", default=True, type=bool)
        args = parser.parse_args()

        return (
            args["person_id"],
            args["comment"],
            args["name"],
            args["revision"],
            args["change_status"],
        ) """
movie_parser: RequestParser = RequestParser()
movie_parser.add_argument(name="id", type=int)
movie_parser.add_argument(name="title", type=str, required=False)
movie_parser.add_argument(name="description", type=str, required=False)
movie_parser.add_argument(name="trailer", type=str, required=False)
movie_parser.add_argument(name="year", type=int, required=False)
movie_parser.add_argument(name="rating", type=float, required=False)
movie_parser.add_argument(name="genre_id", type=int, required=False)
movie_parser.add_argument(name="director_id", type=int, required=False)
