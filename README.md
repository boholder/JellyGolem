# ![jg-icon](/jellygolem/resource/icon/Icon-64.png) Jelly Golem 

~~A chat bot with simulated emotionally oriented responses.~~

Still in development,
 just backing up a copy of the code on the Internet. 
 
I just finished emotion processing part, 
 it's based on a theoretical model of emotion called
 [Robert Plutchik's 'Wheel of Emotions'](https://positivepsychology.com/emotion-wheel/).
And I also wrote a GUI to show how this part works.

## Brief intro (about design ideas)

The aim of this project is to implement a set of "Ghost" side functions (interaction system),
 to the existing "Ukagaka"(desktop partner) "Shell" side projects
 (mostly written in JavaScript, TypeScript, taking advantage of the front-end language 
 with rich and flexible animation)
 ([search results on github](https://github.com/search?q=Ukagaka&type=Repositories)).

The core function of this project, is the implementation of an "event-driven conversation function".
Using event-trigger-based rather than user-input-keyword
 to trigger dialogs, avoids the necessity to write keyword system
 with never-having-enough keyword-response pairs.
Some responses apply to many events, such as perfunctory and ambiguous responses.
I just need to query in the database for responses,
 that match both the corresponding event label and the corresponding reaction emotion label.
Also, because this response design loses user initiative,
 I need to ensure that it will not activated unnecessarily, to avoid disturbing the user.

This project still counts as an entertaining game
 rather than a development library.

## TO-DO

1. ~~emotion processing~~ -20200626
2. dialog process with "emotionlly decision"
3. event generator (based on listening for external events,
 or user-initiated stimuli, such as the "Shell" gaining focus)
4. API, (project can be used when this part is finished)
5. etc, maybe a plugin system,
 then I can use an external NLP ML model to enhance the conversation function.

## Preview

![emotion-processing-test](/doc/screenshot/emotion-test-screenshot.jpg)

1. emotion processing test screenshot

## Functions

## Installation

## Development

## Credits

* Icon prototype made by 
[Freepik from www.flaticon.com](https://www.flaticon.com/free-icon/jelly_184579)