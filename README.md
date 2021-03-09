### spotibot


#### To Do

* ~~Add artists app.~~
* ~~Add albums app (link with artist).~~
* ~~Add tracks app (link with artist and list of features).~~
* ~~Add history app (link with tracks).~~
* ~~Add swagger app.~~
* ~~Add song parser method to parse spotify response and save everything as it goes.~~  
* Add heartbeat app (🌿 yahaha).
* ~~Add permission_class for api_key param.~~  
* ~~Add spotify integration.~~
* ~~Add jobs app.~~
* ~~Add job for history playlist update and saving.~~ (every 30 minutes).
* ~~Add job for discover playlist update.~~ (every hour)
* Add job for weeklys playlist update. (every sunday at 23:59)
* ~~Add service to inject history elements.~~
* ~~Add settings for prod.~~
* Add configuration for supervisor.
* ~~Add jenkins job for deploy~~.
* Add github hook for jenkins deploy.
* Add spotibot user/database to prod.
* Add cron jobs for jobs.
* Add fail2ban config.



History Job:
  * Read last 50 songs played, save them to database and store them into history playlist.

Discover Job:
  * Get last 10 saved songs, get top 3 from each album and put all into the discover playlist.

Weeklys 2021 Job:
  * Get most played song from each week, save each top 3 into the weeklys playlist.


Prod Settings:

* DATABASE_NAME
* DATABASE_USER
* DATABASE_PASSWORD
* DATABASE_HOST
* DATABASE_PORT

* DEBUG
* LOG_LEVEL

* SPOTIFY_USERNAME
* SPOTIFY_CLIENT_ID
* SPOTIFY_CLIENT_SECRET
* SPOTIFY_PLAYLISTS_DISCOVER
* SPOTIFY_PLAYLISTS_HISTORY
