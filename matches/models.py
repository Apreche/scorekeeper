from django.db import models

class Match(models.Model):
    date = models.DateTimeField()
    game = models.ForeignKey('games.Game')
    players = models.ManyToManyField('players.Player', through='Play')
    asterisk = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s - %s" % (game, date)

PLAY_RESULTS = (
    ('W', 'Win'),
    ('L', 'Lose'),
    ('D', 'Draw'),
    ('F', 'Forefeit'),
)

class Play(models.Model):
    score = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=PLAY_RESULTS)
    player = models.ForeignKey('players.Player')
    match = models.ForeignKey('matches.Match')
