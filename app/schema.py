from datetime import datetime
from typing import Dict, Union

import graphene
import graphql
from graphene_sqlalchemy import SQLAlchemyConnectionField

import schema_matches
from database.base import db_session
from database.model import ModelMatches


class Query(graphene.ObjectType):
    """Query objects for GraphQL API."""

    node = graphene.relay.Node.Field()
    matches = graphene.List(schema_matches.Matches,
        match_id=graphene.Argument(type=graphene.String, required=True),
    )
    matchesList = SQLAlchemyConnectionField(schema_matches.Matches)
    findMatch = graphene.List(schema_matches.Matches,
        date=graphene.Argument(type=graphene.String, required=True),
    )

    @staticmethod
    def resolve_matches(args, info, match_id=None):
        match = db_session.query(ModelMatches).filter_by(match_id=match_id).all()
        return match

    @staticmethod
    def resolve_findMatch(args: Dict,
        info: graphql.execution.base.ResolveInfo,
        date: Union[str, None] = None):

        date = datetime.strptime(date, '%Y-%m-%d')
        match = db_session.query(ModelMatches).filter_by(match_date=date).all()

        return match



class Mutation(graphene.ObjectType):
    createMatch = schema_matches.CreateMatch.Field()
    updateMatch = schema_matches.UpdateMatch.Field()
    deleteMatch = schema_matches.DeleteMatch.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
