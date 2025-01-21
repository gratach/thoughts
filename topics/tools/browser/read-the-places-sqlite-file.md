# Read the places.sqlite file

The `places.sqlite` file that [can be obtained from firefox](how-to-archive-the-browser-history.md) can be opened with the [sqlitebrowser](https://sqlitebrowser.org/).
Navigate to the tab "browse data". You can select the table in the drop-down menu.

The table `moz_historyvisits` contains all visits of pages with the date information in the column `visit_date`. This information is encoded as [unix time](https://en.wikipedia.org/wiki/Unix_time). Convert it to human readable date time with [this converter](https://unixtime.org/) or in the command line with `date -d @1234567890`where `1234567890` should be replaced by the time stamp with the last six digits removed.

The visited URLs are saved in the table `moz_places`.
