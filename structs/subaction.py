from utility import to_word
from random import randint as rng
from structs.allow_iasa import AllowIASA
from structs.async_timer import AsyncTimer
from structs.aura import Aura
from structs.autocancel import Autocancel
from structs.body_state import BodyState
from structs.continuation_control import ContinuationControl
from structs.execute_loop import ExecuteLoop
from structs.gfx import GFX
from structs.goto import GoTo
from structs.hitbox import Hitbox
from structs.invincibility import Invincibility
from structs.model_mod import ModelMod
from structs.partial_invincibility import PartialInvincibility
from structs.psuedo_random_sfx import PseudoRandomSFX
from structs.random_smash_sfx import RandomSmashSFX
from structs.return_to import ReturnTo
from structs.reverse_direction import ReverseDirection
from structs.rumble import Rumble
from structs.self_damage import SelfDamage
from structs.set_all_bone_states import SetAllBoneStates
from structs.set_bone_state import SetBoneState
from structs.set_flag import SetFlag
from structs.set_loop import SetLoop
from structs.sfx_and_gfx import SFXAndGFX
from structs.sfx import SFX
from structs.smash_charge import SmashCharge
from structs.spawn_article import SpawnArticle
from structs.subroutine import Subroutine
from structs.sync_timer import SyncTimer
from structs.throw import Throw
from structs.toggle_flag import ToggleFlag
from structs.unknown import Unknown
from structs.windeffect import WindEffect

all_subactions = []

class Subaction():
    def __init__(self, subaction_data, dat_file, index):
        self.dat_file = dat_file
        self.data = subaction_data
        self.index = index
        self.friendly_name = "Nameless"
        self.name = self.get_name()
        self.script = []
        self.unknowns = []
        self.sync_timers = []
        self.async_timers = []
        self.set_loops = []
        self.execute_loops = []
        self.gotos = []
        self.returns = []
        self.subroutines = []
        self.gfx = []
        self.hitboxes = []
        self.specific_hurtbox_invincibilities = []
        self.invincibilities = []
        self.sfx = []
        self.random_sfx = []
        self.auto_cancels = []
        self.reverse_directions = []
        self.allow_iasas = []
        self.spawn_articles = []
        self.change_body_states = []
        self.set_bone_states = []
        self.set_specific_bone_states = []
        self.toggle_followup_flags = []
        self.set_followup_flags = []
        self.model_mods = []
        self.throws = []
        self.pseudo_random_sfx = []
        self.rumbles = []
        self.auras = []
        self.self_damages = []
        self.continuation_controls = []
        self.gfx_and_sfx = []
        self.smash_charges = []
        self.wind_effects = []
        self.caught_by_unhandled = []
        self.get_events(self.events_offset())
        all_subactions.append(self)

    def __str__(self):
        string  = ""
        string += "Subaction Index: " + str(self.index) + "\n"
        string += "Subaction Name: " + str(self.name) + "\n"
        string += "Friendly Name: " + self.friendly_name + "\n"
        for i, event in enumerate(self.script):
            string += "Event " + str(i) + ": " + event.__str__() + "\n"
        return string

    def name_offset(self):
        return to_word(self.data, 5)
    
    def animation_offset(self):
        return to_word(self.data, 4)

    def animation_size(self):
        return to_word(self.data, 3)

    def events_offset(self):
        return to_word(self.data, 2)

    def position_flags(self):
        return to_word(self.data, 1)

    def character_id(self):
        return to_word(self.data, 0)

    def get_name(self):
        return self.dat_file.get_string(self.name_offset())

    def get_events(self, offset):
        file_data = self.dat_file.data_block
        command = file_data[offset]
        command = command >> 2
        command = command << 2
        size = 0x04
        match command: # This pattern could probably be implemented better but not a huge deal
            case 0x00: #?
                size = 0x04
                unk = Unknown(file_data[offset:offset+size], offset)
                self.unknowns.append(unk)
                self.script.append(unk)
                return
            case 0x04: # Sync Timer
                size = 0x04
                sync = SyncTimer(file_data[offset:offset+size], offset)
                self.sync_timers.append(sync)
                self.script.append(sync)
            case 0x08: # Async Timer
                size = 0x04
                _async = AsyncTimer(file_data[offset:offset+size], offset)
                self.async_timers.append(_async)
                self.script.append(_async)
            case 0x0C: # Set Loop
                size = 0x04
                s_loop = SetLoop(file_data[offset:offset+size], offset)
                self.set_loops.append(s_loop)
                self.script.append(s_loop)
            case 0x10: # Execute Loop
                size = 0x04
                e_loop = ExecuteLoop(file_data[offset:offset+size], offset)
                self.execute_loops.append(e_loop)
                self.script.append(e_loop)
            case 0x14: # Go To 
                size = 0x08
                goto = GoTo(file_data[offset:offset+size], offset)
                self.gotos.append(goto)
                self.script.append(goto)
            case 0x18: # Return
                size = 0x04
                _return = ReturnTo(file_data[offset:offset+size], offset)
                self.returns.append(_return)
                self.script.append(_return)
            case 0x1C: # Call Subroutine
                size = 0x08
                subroutine = Subroutine(file_data[offset:offset+size], offset)
                self.subroutines.append(subroutine)
                self.script.append(subroutine)
            case 0x28: # GFX
                size = 0x14
                gfx = GFX(file_data[offset:offset+size], offset)
                self.gfx.append(gfx)
                self.script.append(gfx)
            case 0x2C: # Hitbox
                size = 0x14
                hitbox = Hitbox(file_data[offset:offset+size], offset)
                self.hitboxes.append(hitbox)
                self.script.append(hitbox)
            case 0x3C: # Specific Hurtbox Invincibility
                size = 0x04
                hurtbox_intang = PartialInvincibility(file_data[offset:offset+size], offset)
                self.specific_hurtbox_invincibilities.append(hurtbox_intang)
                self.script.append(hurtbox_intang)
            case 0x40: # Invincibility
                size = 0x04
                invincibility = Invincibility(file_data[offset:offset+size], offset)
                self.invincibilities.append(invincibility)
                self.script.append(invincibility)
            case 0x44: # SFX
                size = 0x0C
                sfx = SFX(file_data[offset:offset+size], offset)
                self.sfx.append(sfx)
                self.script.append(sfx)
            case 0x48: # Random Smash SFX
                size = 0x04
                random_sfx = RandomSmashSFX(file_data[offset:offset+size], offset)
                self.random_sfx.append(random_sfx)
                self.script.append(random_sfx)
            case 0x4C: # Autocancel
                size = 0x04
                autocancel = Autocancel(file_data[offset:offset+size], offset)
                self.auto_cancels.append(autocancel)
                self.script.append(autocancel)
            case 0x50: # Reverse Direction
                size = 0x04
                reverse = ReverseDirection(file_data[offset:offset+size], offset)
                self.reverse_directions.append(reverse)
                self.script.append(reverse)
            case 0x5C: # Allow IASA
                size = 0x04
                iasa = AllowIASA(file_data[offset:offset+size], offset)
                self.allow_iasas.append(iasa)
                self.script.append(iasa)
            case 0x60: # Generate Article???
                size = 0x04
                article = SpawnArticle(file_data[offset:offset+size], offset)
                self.spawn_articles.append(article)
                self.script.append(article)
            case 0x68: # Body State
                size = 0x04
                bodystate = BodyState(file_data[offset:offset+size], offset)
                self.change_body_states.append(bodystate)
                self.script.append(bodystate)
            case 0x6C: # Set All Bones State
                size = 0x04
                bones = SetAllBoneStates(file_data[offset:offset+size], offset)
                self.set_bone_states.append(bones)
                self.script.append(bones)
            case 0x70: # Set Specific Bone State
                size = 0x04
                bone = SetBoneState(file_data[offset:offset+size], offset)
                self.set_specific_bone_states.append(bone)
                self.script.append(bone)
            case 0x74: # Toggle Followup Flag
                size = 0x04
                toggle = ToggleFlag(file_data[offset:offset+size], offset)
                self.toggle_followup_flags.append(toggle)
                self.script.append(toggle)
            case 0x78: # Set Followup Flag
                size = 0x04
                set_flag = SetFlag(file_data[offset:offset+size], offset)
                self.returns.append(set_flag)
                self.script.append(set_flag)
            case 0x7C: # Model Mod
                size = 0x04
                model_mod = ModelMod(file_data[offset:offset+size], offset)
                self.model_mods.append(model_mod)
                self.script.append(model_mod)
            case 0x88: # Throws
                size = 0x0C
                throw = Throw(file_data[offset:offset+size], offset)
                self.throws.append(throw)
                self.script.append(throw)
            case 0x98: # Psuedo Random SFX
                size = 0x1C
                psuedo = PseudoRandomSFX(file_data[offset:offset+size], offset)
                self.pseudo_random_sfx.append(psuedo)
                self.script.append(psuedo)
            case 0x9C: # ? It's large, probably does something...
                size = 0x10
                unk = Unknown(file_data[offset:offset+size], offset)
                self.unknowns.append(unk)
                self.script.append(unk)
            case 0xAC: # Rumble
                size = 0x04
                rumble = Rumble(file_data[offset:offset+size], offset)
                self.rumbles.append(rumble)
                self.script.append(rumble)
            case 0xB8: # Body Aura
                size = 0x04
                aura = Aura(file_data[offset:offset+size], offset)
                self.auras.append(aura)
                self.script.append(aura)
            case 0xCC: # Self-Damage
                size = 0x04
                self_damage = SelfDamage(file_data[offset:offset+size], offset)
                self.self_damages.append(self_damage)
                self.script.append(self_damage)
            case 0xD0: # Continuation Control?
                size = 0x04
                continue_control = ContinuationControl(file_data[offset:offset+size], offset)
                self.continuation_controls.append(continue_control)
                self.script.append(continue_control)
            case 0xD8: # ????
                size = 0x0C
                unk = Unknown(file_data[offset:offset+size], offset)
                self.unknowns.append(unk)
                self.script.append(unk)
            case 0xDC: # SFX and GFX
                size = 0x0C
                sfx_and_gfx = SFXAndGFX(file_data[offset:offset+size], offset)
                self.gfx_and_sfx.append(sfx_and_gfx)
                self.script.append(sfx_and_gfx)
            case 0xE0: # Smash Charge
                size = 0x08
                charge = SmashCharge(file_data[offset:offset+size], offset)
                self.smash_charges.append(charge)
                self.script.append(charge)
            case 0xE8: # Aesthetic Wind Effect
                size = 0x10
                wind = WindEffect(file_data[offset:offset+size], offset)
                self.wind_effects.append(wind)
                self.script.append(wind)
            case _: # Anything else
                size = 0x04
                unk = Unknown(file_data[offset:offset+size], offset)
                self.unknowns.append(unk)
                self.script.append(unk)
                self.caught_by_unhandled.append(unk)

        self.get_events(offset+size)

    def write_events(self):
        for event in self.script:
            self.dat_file.file_data[event.offset+0x20:event.offset+len(event.data)+0x20] = event.data

def shuffle_subactions(sub_a, sub_b):
    sub_a.data, sub_b.data = sub_b.data, sub_a.data
