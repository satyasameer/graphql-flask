from datetime import datetime

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

import utils
from database.base import db_session
from database.model import ModelMatches


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MatchAttribute:
    match_name = graphene.String(description="Who played in the match.")
    match_date = graphene.String(
        description="When it will be played/was played.")
    match_score = graphene.String(description="Match score.")
    match_status = graphene.String(description="live/finished")


class Matches(SQLAlchemyObjectType, MatchAttribute):
    """People node."""

    class Meta:
        model = ModelMatches
        interfaces = (graphene.relay.Node,)


class CreateMatchInput(graphene.InputObjectType, MatchAttribute):
    """Arguments to create a match."""
    pass


class CreateMatch(graphene.Mutation):
    """Mutation to create a match."""
    match = graphene.Field(
        lambda: Matches, description="Match created by this mutation.")

    class Arguments:
        input = CreateMatchInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['match_date'] = datetime.strptime(
                data['match_date'], '%Y-%m-%d %H:%M:%S')

        match = ModelMatches(**data)
        db_session.add(match)
        db_session.commit()

        return CreateMatch(match=match)

class UpdateMatchInput(graphene.InputObjectType, MatchAttribute):
    """Arguments to update a match."""
    id = graphene.ID(required=True, description="Id of the match.")


class UpdateMatch(graphene.Mutation):
    """Update a match."""
    match = graphene.Field(lambda: Matches, description="Match updated by this mutation.")

    class Arguments:
        input = UpdateMatchInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['match_date'] = datetime.strptime(
                data['match_date'], '%Y-%m-%d %H:%M:%S')

        match = db_session.query(ModelMatches).filter_by(id=data['id'])
        match.update(data)
        db_session.commit()
        match = db_session.query(ModelMatches).filter_by(id=data['id']).first()

        return UpdateMatch(match=match)


class DeleteMatchInput(graphene.InputObjectType, MatchAttribute):
    """Arguments to delete a match."""
    id = graphene.ID(required=True, description="Id of the match.")


class DeleteMatch(graphene.Mutation):
    """Delete a match."""
    match = graphene.Field(lambda: Matches, description="Match deleted by this mutation.")

    class Arguments:
        input = DeleteMatchInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        match = ModelMatches(**data)
        db_session.query(ModelMatches).filter_by(id=data['id']).delete()
        db_session.commit()

        return DeleteMatch(match=match)
