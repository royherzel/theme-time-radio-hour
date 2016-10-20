from archive.models import db
from archive.models.mixin import Mixin
from datetime import datetime


class EpisodesActions():
    def add(newEpisode, tags=None):
        Mixin.create(newEpisode)
        if tags:
            if type(tags) is not list:
                raise TypeError("tags must be list")
            else:
                for tag in tags:
                    Mixin.create(EpisodesTags(tag=tag, episode_id=newEpisode.id))


class Episodes(db.Model, EpisodesActions):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.Unicode())
    date_pub = db.Column(db.DateTime)
    media = db.Column(db.String())
    image = db.Column(db.String())

    def __repr__(self):
        return '<Episode ({}): {}>'.format(self.id, self.title)


class EpisodesTags(db.Model):
    tag = db.Column(db.String(), primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), primary_key=True)
    episode = db.relationship('Episodes', backref=db.backref('tags', lazy='dynamic'))


class TracksActions():
    def add(newTrack, tags=None):
        Mixin.create(newTrack)
        if tags:
            if type(tags) is not list:
                raise TypeError("tags must be list")
            else:
                for tag in tags:
                    Mixin.create(TracksTags(tag=tag, track_id=newTrack.id))


class TracksTags(db.Model):
    tag = db.Column(db.String(), primary_key=True)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), primary_key=True)
    track = db.relationship('Tracks', backref=db.backref('tags', lazy='dynamic'))


class Tracks(db.Model, TracksActions):
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))
    episode = db.relationship('Episodes', backref=db.backref('tracklist', lazy='dynamic'))
    title = db.Column(db.String())
    parsed_song = db.Column(db.String())
    parsed_artist = db.Column(db.String())
    position = db.Column(db.Integer)
    resolved = db.Column(db.Boolean)

    def __repr__(self):
        return '<Track ({}): {}>'.format(self.id, self.title)
