· ·:·: Introduction to the Mind Stone :·:· ·
=====

.. _scripttutorial:

Intro
------------

In this tutorial you will learn
^^^^^^^^^^^^

To use the Mind Stone to auto-farm Deadwood Canyon

Estimated time to complete:
^^^^^^^^^^^^

20 minutes

Prior knowledge required:
^^^^^^^^^^^^

* Play Stone Story RPG until you defeat Nagaraja.
* Understand the strategic value of changing weapons in the middle of a location.
* Build the Cauldron and understand the Healing Potion.
* Understand that the Ouroboros causes locations to loop around.

Items needed:
^^^^^^^^^^^^

* Sword, Shield and Crossbow with at least 4-stars each.
* 80 Tar for potions.
* Auto-refill enabled on your Cauldron.

The Mind Stone is an incredibly powerful relic. Its purpose is to automate actions, such as changing weapons and using potions in the middle of a run. 
Instructions feed into the game's AI and tell it what to do. The Mind Stone, if setup correctly, leads to super-human actions as your character 
immediatly adapts to changes in the game.

This relic is also Stone Story's gate to customization and cosmetics. Explore work done by other players and even create your own! 
There are pets, hats, custom interface, entire mini-games and more. `Learn about cosmetics and modding here <https://steamcommunity.com/sharedfiles/filedetails/?id=2003221477>`_.

Instructions in the Mind Stone are written in Stonescript, a minimalist language designed for use by everyone. 
If you can type, you can Stonescript--no programming degree required! However, if you'd like to dive into the deep end, 
see the :doc:`documentation` where all available instructions are listed in detail, along with examples.

Need help? Want to collaborate on scripts? Visit `our Discord <https://discord.gg/StoneStoryRPG>`_.

Let's get started!

·:·:· 1. Clear the Mind Stone ·:·:·
------------

Select all the text that comes by default in your Mind Stone and delete it. If you'd like, you could keep the header by *Bezerra, the Sage*, as any text preceeded by ``//`` has no effect and is ignored by the AI.

Hint: The shortcut to select all is Ctrl + A.
.. code-block::
          _.,·─·──·────┬───────────────────────·──·─·.,_
       .:´             |                                `-.
     .:'               └--------┐                Power     `.
    /:'                         |          ____,---╓───┐    `\
   ,:'                          ◘         │    '---╙───┘      \
   :'                                     |                   `.
  :.'  ╔══════════════════════════════════╧═══════════════╕    |
  :.|  ║                                                  │   '/
  :.!  ║                                                  │   ´!
  :.   ║                                                  │    |
  :.'  ║                                                  │   '|
  :.   ║                                                  │    |
  :.'  ║                                                  │   '|
  :.   ║                                                  │    |
  !.'  ║                                                  │   '|
  :.   ║                                                  │    |
  :.'  ║                                                  │   '|
  :.|  ║                                                  │    |
  :.'  ║                                                  │   '|
  :.   ║                                                  │   .(
  :.'  ║                                                  │   '|
  :.   ║                                                  │    |
  :.'  ║                                                  │   '|
  :.|  ║                                                  │    |
  :.'  ╙────────────────────────┬─────────────────────────┘   ';
  ':.\           .              |              .             ./
   '::.`-        |              °              |            .'
     '':.:.:.:.:.|.:.:.:.:.:.:.:.:.:.:.:.:.:.:.|.:.:.:.:.:·`

·:·:· 2. Healing ·:·:·
------------
.. code-block::
    )(
   (~≈)
    ¯¯

Instructions are all about converting common sense into something the game's AI can understand. 
For example, if you're about to die it would make sense to use a Healing Potion, right?

There's a command to do that. Type the following into the Mind Stone:

.. code-block::

   activate potion

This tells the AI what to do. When you visit a location it will continuously try to activate the potion, every frame. 
As soon as you lose some health it will then successfully activate. In case you have a non-healing potion such as Lucky Potion, 
then it will activate immediately when you visit a location. 
Probably not the outcome we're looking for, so let's improve it.

We can think of a more complete instruction like this:

.. code-block::

   "IF my hitpoints are low THEN activate potion"

Translating that into Stonescript, modify the Mind Stone to the following:

.. code-block::

   ?hp < 7
      activate potion

The first line ``?hp < 7`` is asking a question, ``"Are my hitpoints less-than 7?"`` As opposed to human language, 
the game requires the question mark as the first thing in the line, this way it knows right away that it's 
a question and knows how to read the rest (¿kinda like Spanish?).

Notice the space added in front of ``activate potion``. The space is important because it groups that line as dependant to the line above it. 
This way, it will only activate if the question above equals ``"yes"``.

·:·:· 3. Play ·:·:·
------------
.. code-block::
    \|' /´,  
    `|    /  ,
    /\ /  `-´-
    \ò ó` /´  
    |   , (   
    '¡'!| |   
    |-'´ _'-. 
   ¯'_/`´·\  `

With your Mind Stone powered up and a potion freshly brewed, head over to any dangerous location and watch as you take damage from foes. 
When your hitpoints go below 7 it should automatically activate the potion.

.. note::

   Hint: To re-open the Mind Stone in the middle of a location press ``M``. 
   There's no need to head back to the Workstation. When you close the Mind Stone and resume the location your 
   script will be reloaded and the new instructions you've written will take effect.

·:·:· 4. Weapons ·:·:·
------------
.. code-block::
  │ O__
  ┼/|)_)
   / \

Our goal in this tutorial is to auto-farm Deadwood Canyon. A basic Sword + Shield combo is enough to complete the location on some difficulties and a good starting point.

Add the following to the bottom of your Mind Stone:

.. code-block::

   equipL sword
   equipR shield

The ``equip`` command is exactly what you'd expect. It finds a weapon from your inventory and equips it. 
All text to the right of the command are additional details for the instruction. The ``L`` and ``R`` indicate which hand to place the weapon, 
left or right respectively. You could add more details to specify which weapon to equip, as you probably have many swords in your inventory. 
For example you can add ``*7`` to specify it's a 7-star weapon: ``equipL sword *7``. Without any additional details the AI will find your best 
weapon and equip that, which is probably ok.
.. code-block::
     |/) 
   o.-._ 
  ´ /|`-`
    `'   

This will do fine in general, but when you are against Mosquitos it could be better to equip a Crossbow and avoid all damage, 
as they are very weak but can swarm you and deal lots of damage:

.. code-block::

   ?foe = mosquito
      equip crossbow

The keyword ``foe`` allows us to inspect the enemy currently targeted by the AI and then make decisions based on what kind of foe it is.

You may notice there's no ``L`` or ``R`` on this ``equip`` command. For the Crossbow we'll leave it without any details and let the AI decide what's best. 
Keep things simple for now.

Your entire script should look like this:

.. code-block::

   ?hp < 7
      activate potion

   equipL sword
   equipR shield

   ?foe = mosquito
      equip crossbow


At this point it's worth clarifying that your script executes from top to bottom. It will first check the potion, 
then equip the sword and shield, and finally, if you are facing a mosquito it will equip the crossbow. The whole script runs 30 times per second.

Go to Deadwood Canyon to see if everything is working. If your script is a success and you didn't choose a location 
that's too hard for your current weapons, then you should be able to keep looping the location with the Ouroboros and farm it many times. 
That is, until you run out of Tar for potions or your inventory becomes full with treasure.

·:·:· 5. Wood ·:·:·
------------
.. code-block::
      \|
       |, |/
    \| |  /-'
  `-─\ | /_/─,
      \'//
    '\} {
      { }
      } {
     //\`\

As you approach trees in Deadwood Canyon, perhaps you'd like to take the opportunity to harvest wood.
Add the following to the bottom of your script:

.. code-block::

   ?harvest.distance < 10
      equip hatchet

In this case ``L`` and ``R`` are also not needed because the Hatchet can only be equipped on the right side anyway.

Visit Deadwood to try out your latest changes!

·:·:· 6. More Healing ·:·:·
------------
.. code-block::
         ____,
      _.-·´ o/`___
    ,´  _.-._\¯¯`-.`.
   /  ,´           `.`.
  |  :              | :
  |  :.            .' ;
   \  `':.,,,,,..·´ ,´
     `-._       _,-´
          ¯¯¯¯¯

At this point the script works, but depending on the star level of your gear or the chosen difficulty of the location you may still 
be taking too much damage from foes. Let's improve the script by equipping the Ouroboros, which heals over time while equipped.

Add the following:

.. code-block::
   ?foe ! boss & foe.distance > 8
      equipL ouroboros

The question asked here is more complex, so let's break it down. On line 1, the first part asks ``foe ! boss`` which translates to 
``"Foe is not a boss"``. The exclamation mark is the opposite of the equals symbol.

The second part of line 1 is f``oe.distance > 8`` which means ``"Is the foe's distance to the player greater than 8?"``. 
The two questions in line 1 are combined into a single question with the ``&`` symbol, which means ``"AND"``.

The whole instruction means:

.. code-block::
   "If the next foe is not a boss and it's distance to the player is greater than 8, equip the Ouroboros on the left hand."

.. note::
      Hint: With a foe distance of ``8`` the Ouroboros will be used in combat. This is useful if your gear level is low. 
      However, if ``17`` is used instead of ``8`` then the Ouroboros is excluded from combat, resulting in faster loop times. 
      This is because the Ouroboros has an attack range of ``17``. The value of ``8`` allows the Sword to be prioritized in melee situations.

·:·:· 7. Pickups ·:·:·
------------
.. code-block::
     ,
   _/-'

You may notice that one thing slowing us down are things on the ground that must be picked up. 
In Deadwood Canyon that would be bits of wood. Lucky for us, the Star Stone (when equipped) sucks up all pickups and speeds up movement by a lot.

Add the following:

.. code-block::
   ?pickup.distance < 10
      equipL star

Similar to ``foe.distance`` this instruction is asking if the next pickup is less than ``10`` units away from the player. 
If that's the case then we equip the Star Stone on the left hand. We can say only ``star`` and that's enough to identify 
the relic because there aren't any other items with ``star`` in their name.

·:·:· 8. All Together ·:·:·
------------

Our script for Deadwood is complete! However, these instructions will currently run in all locations. 
We probably want to do a specific set of instructions for each location, so we need to group 
these and only run them if we are exploring Deadwood Canyon.

To check in what location we are, we can use the keyword ``loc``.

At the TOP of the script, add the following:

.. code-block::
   ?loc = deadwood

But also, add space to the front of all the lines thereafter, so they become dependant on the location question. The entire script should look like this:

.. code-block::
   ?loc = deadwood
      ?hp < 7
      activate potion
  
   equipL sword
   equipR shield
   ?foe = mosquito
      equip crossbow
  
   ?harvest.distance < 10
      equip hatchet

   ?foe ! boss & foe.distance > 8
      equipL ouroboros
  
   ?pickup.distance < 10
      equipL star

.. note::
      Hint: You can copy/paste scripts from here or from other players into the Mind Stone with the ``Ctrl+C`` / ``Ctrl+V`` shortcuts.

·:·:· What's next? ·:·:·
------------
.. code-block::
       .-.
       \ ´ .-.
  ,-.   )  \ ´
  '- `-/¯\-´
   .· /`°´\ ·.
   `-´     `-´

External resources and mini-tutorials below.

Links
^^^^^^^^^^^^

Trouble with this tutorial? Need help with other locations? Visit `our Discord <https://discord.gg/StoneStoryRPG>`_.

Discover fun `cosmetics and mini-games <https://steamcommunity.com/sharedfiles/filedetails/?id=2003221477>`_ created by the Stone Story community.

Ready to dive deeper? Learn everything from the :doc:`documentation`.

Lifesteal
^^^^^^^^^^^^

Poison
^^^^^^^^^^^^

Mobility
^^^^^^^^^^^^

Ability Activation
^^^^^^^^^^^^