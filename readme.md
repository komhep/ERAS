# ERAS
EVE online Region Alarm System

*This tool warns if a neutral player(s) approaching the region. The alarm is based on *South East Channel* messages and plays the narration in english: `Enemy in N jumps from the region`. You have to setup the list of the systems manually so the tool works properly (see according section below for this).*

#### Dependencies
- Python 3
- virtualenv
- pip

### Installation
1. Download this repository to your PC (eg. `git clone...`)
1. Create virtual environment
`virtualenv env`
1. Activate virtual environment
`source env/bin/activate`
1. Install dependencies
`pip intall -r requirements.txt`

### Setting up the tool
Settings files are `.txt` files with JSON object inside
##### settings.txt file
Look for `path_to_eve_logs` field - it should contain a valid absolute path to South East Channel log file in Eve logs folder. For example for mac: `Users/YOURNAME/Documents/Eve/Logs/Chatlogs/South East channel_*.txt`
Note: `South East Channel_*.txt` part! It is important it should be like this, don’t change this ending!

##### systems.txt file
The JSON object in the file contains 5 fields with arrays that should be populated with the names of systems. Each field represents the number of jumps to the border of your system.

The example below shows 2 systems that re situated in 4 jumps from the system I wish to set alarm for:
```
{
  "4":[
    "IO-234",
    "K-1G23"
  ]
},
```

### Participation and support
Want to participate or send some ISKs? Feel free to contact `t beta` character in game.
