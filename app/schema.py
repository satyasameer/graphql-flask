from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_matches


class Query(graphene.ObjectType):
    """Query objects for GraphQL API."""

    node = graphene.relay.Node.Field()
    matches = graphene.relay.Node.Field(schema_matches.Matches)
    matchesList = SQLAlchemyConnectionField(schema_matches.Matches)


class Mutation(graphene.ObjectType):
    createMatch = schema_matches.CreateMatch.Field()
    updateMatch = schema_matches.UpdateMatch.Field()
    deleteMatch = schema_matches.DeleteMatch.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
