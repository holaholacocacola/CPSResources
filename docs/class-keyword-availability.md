# Class and Keyword Labels

- [Classes](#classes)
- [Keywords](#keywords)

## Classes

1. The following class labels are available in all class packs. They are currently hardcoded and looked up in CPS dll's'. This will change in a future update.
If making a class pack, these are the labels available to replace.

- ClassAlterationMage
- ClassApothecary
- ClassArcher
- ClassAssassin
- ClassBarbarian
- ClassBard
- ClassBattleMage
- ClassBeggar
- ClassBlackSmith
- ClassChaurus
- ClassChaurusFlyer
- ClassCitizen
- ClassConjurer
- ClassCrusader
- ClassDeathHound
- ClassDestructionMage
- ClassDragon
- ClassDragonPriest
- ClassDuelist
- ClassDwarvenCenturion
- ClassDwarvenSphere
- ClassEnchanter
- ClassFalmer
- ClassFalmerShaman
- ClassFighter
- ClassFoodVendor
- ClassGargoyle
- ClassGiant
- ClassHagraven
- ClassHealer
- ClassHorse
- ClassIceWraith
- ClassIllusionist
- ClassKnight
- ClassLurker
- ClassMammoth
- ClassMiner
- ClassMonk
- ClassMudCrab
- ClassNightblade
- ClassNone
- ClassPredator
- ClassPrey
- ClassRanger
- ClassRogue
- ClassScout
- ClassSorcerer
- ClassSpellSword
- ClassSpider
- ClassTank
- ClassThief
- ClassVampire
- ClassWarmonger
- ClassWarrior
- ClassWerewolf
- ClassWitchblade
- ClassWizard

Class icons are determined by the following priority:

- Name Match
- Skill Weight Match
	
A name match hit occurs when an actor class' FULL NAME matches a vanilla class name.
Skill Weights occurs f there is no name match. First an actors class skill weights are gathered for all skills > 2. These are then looked up in a cross class table for a match followed by a single class lookup if there is no match.
	
### Single Skill Class Table:

- ClassAlterationMage : Alteration
- ClassArcher         : Archery
- ClassConjurer       : Conjuration
- ClassDestructionMage: Destruction
- ClassIllusionist    : Illusion
- ClassHealer         : Restoration
- ClassDuelist        : One Handed
- ClassFighter        : Two Handed

### Cross Class Skill Table:

- ClassBattleMage  : One Handed   + (Alteration | Destruction)
- ClassBarbarian   : Light Armor  + Two Handed
- ClassCrusader    : Heavy Armor  + Restoration
- ClassHealer      : Restoration  + Speech
- ClassKnight      : Heavy Armor  + OneHanded
- ClassMonk        : Alteration   + Restoration
- ClassNightblade  : Destruction  + Sneak || (LightArmor + Restoration)
- ClassRanger      : Archery      + Light Armor
- ClassRogue       : OneHanded    + Sneak
- ClassScout       : Archery      + Sneak
- ClassSorcerer    : Illusion     + (Destruction | Alteration)
- ClassSpellSword  : Alteration   + (Heavy Armor | Light Armor | Two Handed)
- ClassSpellSword  : Destruction  + (Heavy Armor | Light Armor | Two Handed)
- ClassSpellSword  : Illusion     + (Heavy Armor | Light Armor)
- ClassWarmonger   : Heavy Armor  + Two Handed
- ClassWarrior     : One Handed   + (Block | Two Handed)
- ClassWizard      : Conjuration  + Destruction
- ClassTank        : Block        + Heavy Armor
- ClassThief       : Light armor  + Sneak

In most cases, vanilla npcs will end up with a class match. If not, use the override file (cps/overrides) to force them to a specific class.

## Keywords

The following keywords are available in all keyword packs. These lookups are currently hardcoded and looked up in CPS dll's. This will change in a future update.
If making a keyword pack, these are the labels available to replace.

- ActorTypeAnimal
- ActorTypeDaedra
- ActorTypeDragon
- ActorTypeDwarven
- ActorTypeGhost
- ActorTypeGiant
- ActorTypeTroll
- ActorTypeUndead
- ActorTypeVampire