import fighter
from iso import DAT
from structs import hitbox

kirby = fighter.Fighter("Kirby", DAT(b'PlKb.dat'))
fighter.fighters.append(kirby)
kirby.fighter_id = 0x04

kirby.special_attribute_block_size = 0x424
kirby.articles_sizes = [0x10]
kirby.articles_offsets = [0x7B2C]
kirby.projectile_offsets = [0x7B7C]

file_data = kirby.dat_file.file_data
offset = kirby.projectile_offsets[0]
final_cutter_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
final_cutter_hitbox.tags.append("projectile")
kirby.projectile_hitboxes.append(final_cutter_hitbox)

kirby.subactions[322].friendly_name = "Hammer (Ground)"
kirby.subactions[323].friendly_name = "Hammer (Aerial)"
kirby.subactions[325].friendly_name = "Final Cutter"
kirby.subactions[336].friendly_name = "Stone"
kirby.subactions[368].friendly_name = "Copy Falcon Punch (Ground)"
kirby.subactions[369].friendly_name = "Copy Falcon Punch (Aerial)"
kirby.subactions[388].friendly_name = "Copy Ice Shot"
kirby.subactions[393].friendly_name = "Copy Giant Punch (Ground) (Uncharged)"
kirby.subactions[394].friendly_name = "Copy Giant Punch (Ground) (Charged)"
kirby.subactions[398].friendly_name = "Copy Giant Punch (Aerial) (Uncharged)"
kirby.subactions[399].friendly_name = "Copy Giant Punch (Aerial) (Charged)"
kirby.subactions[400].friendly_name = "Copy Nayru's Love"
kirby.subactions[412].friendly_name = "Copy Rollout 1 (Ground)"
kirby.subactions[413].friendly_name = "Copy Rollout 2 (Ground)"
kirby.subactions[414].friendly_name = "Copy Rollout 3 (Ground)"
kirby.subactions[420].friendly_name = "Copy Rollout 1 (Aerial)"
kirby.subactions[421].friendly_name = "Copy Rollout 2 (Aerial)"
kirby.subactions[422].friendly_name = "Copy Rollout 3 (Aerial)"
kirby.subactions[429].friendly_name = "Copy Shield Breaker (Uncharged)"
kirby.subactions[430].friendly_name = "Copy Shield Breaker (Charged)"
kirby.subactions[436].friendly_name = "Copy Shadow Ball (Charging)"
kirby.subactions[445].friendly_name = "Copy Sausage"
kirby.subactions[463].friendly_name = "Copy Warlock Punch (Ground)"
kirby.subactions[464].friendly_name = "Copy Warlock Punch (Aerial)"
kirby.subactions[467].friendly_name = "Copy Flare Blade (Uncharged)"
kirby.subactions[468].friendly_name = "Copy Flare Blade (Charged)"


attribute_data = kirby.dat_file.get_special_attribute_data(kirby.special_attribute_block_size)
kirby.add_attribute(attribute_data, 0x00, "Copy Jumps Turn Duration", 1)
kirby.get_attribute("Copy Jumps Turn Duration").integer = True
kirby.add_attribute(attribute_data, 0x04, "Copy Jumps Horizontal Momentum Backward", 1)
kirby.add_attribute(attribute_data, 0x08, "Copy Jumps Horizontal Momentum Forward", 1)
kirby.add_attribute(attribute_data, 0x0C, "Copy Jumps Turn Momentum", 1)
kirby.add_attribute(attribute_data, 0x10, "Copy Jumps Horizontal Momentum Neutral", 1)
kirby.add_attribute(attribute_data, 0x14, "Copy Jump 1 Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0x18, "Copy Jump 2 Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0x1C, "Copy Jump 3 Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0x20, "Copy Jump 4 Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0x24, "Copy Jump 5 Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0x28, "Copy Number of Jumps", 1)
kirby.get_attribute("Copy Number of Jumps").integer = True
kirby.add_attribute(attribute_data, 0x44, "Copy Inhale Gravity of Inhaled Player", 1)
kirby.add_attribute(attribute_data, 0x48, "Copy Inhale Velocity of Outer Grab Box", 1)
kirby.add_attribute(attribute_data, 0x4C, "Copy Inhale Velocity of Inner Grab Box", 1)
kirby.add_attribute(attribute_data, 0x50, "Copy Inhale Speed", 1)
kirby.add_attribute(attribute_data, 0x54, "Copy Inhale Breakout Resistance", 1)
kirby.add_attribute(attribute_data, 0x58, "Copy Inhale Duration Divisor", 1)
kirby.add_attribute(attribute_data, 0x5C, "Copy Inhale Base Duration", 1)
kirby.add_attribute(attribute_data, 0x60, "Copy Inhale Star Deceleration Rate", 1)
kirby.add_attribute(attribute_data, 0x64, "Copy Inhale Star Duration Divisor", 1)
kirby.add_attribute(attribute_data, 0x68, "Copy Inhale Star Base Duration", 1)
kirby.add_attribute(attribute_data, 0x6C, "Copy Inhale Star Swallow Duration", 1)
kirby.add_attribute(attribute_data, 0x70, "Copy Inhale Star Spin Animation Duration", 1)
kirby.add_attribute(attribute_data, 0x7C, "Copy Inhale Walk Speed", 1)
kirby.add_attribute(attribute_data, 0x80, "Copy Inhale Jump Height", 1)
kirby.add_attribute(attribute_data, 0x84, "Copy Inhale Stop Momentum", 1)
kirby.add_attribute(attribute_data, 0x88, "Copy Inhale Spit Horizontal Velocity", 1)
kirby.add_attribute(attribute_data, 0x8C, "Copy Inhale Spit Velocity Deceleration Rate", 1)
kirby.add_attribute(attribute_data, 0x90, "Copy Inhale Spit Release Angle", 1)
kirby.add_attribute(attribute_data, 0x94, "Copy Inhale Swallow Star Vertical Velocity", 1)
kirby.add_attribute(attribute_data, 0x98, "Copy Inhale Swallow Star Gravity", 1)
kirby.add_attribute(attribute_data, 0x9C, "Copy Inhale Spit Star Release Opponent Horizontal Velocity", 1)
kirby.add_attribute(attribute_data, 0xA0, "Copy Inhale Spit Star Release Opponent Vertical Velocity", 1)
kirby.add_attribute(attribute_data, 0xB0, "Copy Inhale Copy Ability Lose Odds", 1)
kirby.add_attribute(attribute_data, 0xCC, "Copy Hammer Aerial Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0xD0, "Copy Hammer Landing Lag", 1)
kirby.add_attribute(attribute_data, 0xD4, "Copy Final Cutter Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0xD8, "Copy Final Cutter Horizontal Momentum", 1)
kirby.add_attribute(attribute_data, 0xDC, "Copy Final Cutter X-Offset of Projectile", 1)
kirby.add_attribute(attribute_data, 0xE0, "Copy Final Cutter Y-Offset of Projectile", 1)
kirby.add_attribute(attribute_data, 0xEC, "Copy Stone Max Duration", 1)
kirby.get_attribute("Copy Stone Max Duration").integer = True
kirby.add_attribute(attribute_data, 0xF0, "Copy Stone Minimum Duration", 1)
kirby.get_attribute("Copy Stone Minimum Duration").integer = True
kirby.add_attribute(attribute_data, 0xFC, "Copy Stone Slide Acceleration", 1)
kirby.add_attribute(attribute_data, 0x100, "Copy Stone Slide Max Speed", 1)
kirby.add_attribute(attribute_data, 0x104, "Copy Stone Gravity", 1)
kirby.add_attribute(attribute_data, 0x108, "Copy Stone HP", 1)
kirby.add_attribute(attribute_data, 0x10C, "Copy Stone Resistance", 1)
kirby.add_attribute(attribute_data, 0x114, "Copy Stone Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x11C, "Copy Flame Breath Recharge Rate: Fuel", 1)
kirby.add_attribute(attribute_data, 0x120, "Copy Flame Breath Recharge Rate: Flame Size", 1)
kirby.add_attribute(attribute_data, 0x124, "Copy Flame Breath Max Fuel", 1)
kirby.add_attribute(attribute_data, 0x168, "Copy Charge Shot Charge Time", 1)
kirby.add_attribute(attribute_data, 0x16C, "Copy Charge Shot Recoil", 1)
kirby.add_attribute(attribute_data, 0x170, "Copy Charge Shot Frames Per Charge Level", 1)
kirby.get_attribute("Copy Charge Shot Frames Per Charge Level").integer = True
kirby.add_attribute(attribute_data, 0x174, "Copy Charge Shot Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x180, "Copy Toad Aerial Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0x184, "Copy Toad Fall Acceleration", 1)
kirby.add_attribute(attribute_data, 0x3FC, "Copy Toad Detection Bubble Size", 1)
kirby.add_attribute(attribute_data, 0x190, "Copy Giant Punch Swings to Fully Charge", 1)
kirby.get_attribute("Copy Giant Punch Swings to Fully Charge").integer = True
kirby.add_attribute(attribute_data, 0x194, "Copy Giant Punch Damage Increase Per Swing", 1)
kirby.get_attribute("Copy Giant Punch Damage Increase Per Swing").integer = True
kirby.add_attribute(attribute_data, 0x198, "Copy Giant Punch Grounded Horizontal Velocity")
kirby.add_attribute(attribute_data, 0x19C, "Copy Giant Punch Landing Lag")
kirby.add_attribute(attribute_data, 0x1A0, "Copy PK Flash Grounded Animation Loop Frames", 1)
kirby.get_attribute("Copy PK Flash Grounded Animation Loop Frames").integer = True
kirby.add_attribute(attribute_data, 0x1A4, "Copy PK Flash Air Animation Loop Frames", 1)
kirby.get_attribute("Copy PK Flash Air Animation Loop Frames").integer = True
kirby.add_attribute(attribute_data, 0x1A8, "Copy PK Flash Falling Acceleration Delay", 1)
kirby.get_attribute("Copy PK Flash Falling Acceleration Delay").integer = True
kirby.add_attribute(attribute_data, 0x1AC, "Copy PK Flash Charge Release Delay", 1)
kirby.get_attribute("Copy PK Flash Charge Release Delay").integer = True
kirby.add_attribute(attribute_data, 0x1B4, "Copy PK Flash Gravity", 1)
kirby.add_attribute(attribute_data, 0x1BC, "Copy PK Flash Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x1C0, "Copy Pikachu Thunder Jolt Ground Spawn X-Offset", 1)
kirby.add_attribute(attribute_data, 0x1C4, "Copy Pikachu Thunder Jolt Ground Spawn Y-Offset", 1)
kirby.add_attribute(attribute_data, 0x1C8, "Copy Pikachu Thunder Jolt Air Spawn X-Offset", 1)
kirby.add_attribute(attribute_data, 0x1CC, "Copy Pikachu Thunder Jolt Air Spawn Y-Offset", 1)
kirby.add_attribute(attribute_data, 0x1D0, "Copy Pikachu Thunder Jolt Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x1C0, "Copy Pichu Thunder Jolt Ground Spawn X-Offset", 1)
kirby.add_attribute(attribute_data, 0x1C4, "Copy Pichu Jolt Ground Spawn Y-Offset", 1)
kirby.add_attribute(attribute_data, 0x1C8, "Copy Pichu Jolt Air Spawn X-Offset", 1)
kirby.add_attribute(attribute_data, 0x1CC, "Copy Pichu Jolt Air Spawn Y-Offset", 1)
kirby.add_attribute(attribute_data, 0x1D0, "Copy Pichu Jolt Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x200, "Copy Falcon Punch Momentum", 1)
kirby.add_attribute(attribute_data, 0x204, "Copy Aerial Falcon Punch Angle Difference", 1)
kirby.add_attribute(attribute_data, 0x208, "Copy Aerial Falcon Punch Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0x214, "Copy Warlock Punch Momentum", 1)
kirby.add_attribute(attribute_data, 0x218, "Copy Aerial Warlock Punch Angle Difference", 1)
kirby.add_attribute(attribute_data, 0x21C, "Copy Aerial Warlock Punch Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0x230, "Copy Fox Blaster Launch Angle", 1)
kirby.add_attribute(attribute_data, 0x234, "Copy Fox Blaster Launch Speed", 1)
kirby.add_attribute(attribute_data, 0x238, "Copy Fox Blaster Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x254, "Copy Falco Blaster Launch Angle", 1)
kirby.add_attribute(attribute_data, 0x258, "Copy Falco Blaster Launch Speed", 1)
kirby.add_attribute(attribute_data, 0x25C, "Copy Falco Blaster Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x268, "Copy Bow Frames For Max Charge", 1)
kirby.add_attribute(attribute_data, 0x26C, "Copy Bow Charge Speed", 1)
kirby.add_attribute(attribute_data, 0x270, "Copy Bow Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x2A8, "Copy Nayru's Love Gravity Delay", 1)
kirby.get_attribute("Copy Nayru's Love Gravity Delay").integer = True
kirby.add_attribute(attribute_data, 0x2AC, "Copy Nayru's Love Momentum Preservation", 1)
kirby.add_attribute(attribute_data, 0x2B0, "Copy Nayru's Love Fall Acceleration", 1)
kirby.add_attribute(attribute_data, 0x404, "Copy Nayru's Love Max Damage Reflectable", 1)
kirby.get_attribute("Copy Nayru's Love Max Damage Reflectable").integer = True
kirby.add_attribute(attribute_data, 0x404, "Copy Nayru's Love Reflection Bubble Size", 1)
kirby.add_attribute(attribute_data, 0x404, "Copy Nayru's Love Reflection Damage Multiplier", 1)
kirby.add_attribute(attribute_data, 0x404, "Copy Nayru's Love Reflection Speed Multiplier", 1)
kirby.add_attribute(attribute_data, 0x2B4, "Copy Rollout Duration", 1)
kirby.get_attribute("Copy Rollout Duration").integer = True
kirby.add_attribute(attribute_data, 0x2BC, "Copy Rollout Start Air Height Offset", 1)
kirby.add_attribute(attribute_data, 0x2C0, "Copy Rollout Bounciness", 1)
kirby.add_attribute(attribute_data, 0x2C8, "Copy Rollout Gravity During Roll", 1)
kirby.add_attribute(attribute_data, 0x2CC, "Copy Rollout Base Rolling Speed", 1)
kirby.add_attribute(attribute_data, 0x2D0, "Copy Rollout Max Rolling Speed", 1)
kirby.add_attribute(attribute_data, 0x2D8, "Copy Rollout Aerial X-Axis Momentum Forward", 1)
kirby.add_attribute(attribute_data, 0x2E0, "Copy Rollout Aerial Initial Momentum", 1)
kirby.add_attribute(attribute_data, 0x2E4, "Copy Rollout Max Momentum", 1)
kirby.add_attribute(attribute_data, 0x2E8, "Copy Rollout Spinning Speed", 1)
kirby.add_attribute(attribute_data, 0x2EC, "Copy Rollout Spinning Turn Speed", 1)
kirby.add_attribute(attribute_data, 0x2F8, "Copy Rollout Bounciness A", 1)
kirby.add_attribute(attribute_data, 0x2FC, "Copy Rollout Bounciness B", 1)
kirby.add_attribute(attribute_data, 0x300, "Copy Rollout Base Damage", 1)
kirby.add_attribute(attribute_data, 0x304, "Copy Rollout Damage Multiplier", 1)
kirby.add_attribute(attribute_data, 0x308, "Copy Rollout Horizontal Bounce On Hit", 1)
kirby.add_attribute(attribute_data, 0x30C, "Copy Rollout Vertical Bounce on Hit", 1)
kirby.add_attribute(attribute_data, 0x310, "Copy Rollout Input Modifier", 1)
kirby.add_attribute(attribute_data, 0x320, "Copy Rollout Charge Rate", 1)
kirby.add_attribute(attribute_data, 0x324, "Copy Rollout Charge Time", 1)
kirby.add_attribute(attribute_data, 0x32C, "Copy Rollout Spin Charge Animation", 1)
kirby.add_attribute(attribute_data, 0x338, "Copy Rollout Speed Variable", 1)
kirby.add_attribute(attribute_data, 0x33C, "Copy Rollout Spin Animation Post Hit", 1)
kirby.add_attribute(attribute_data, 0x340, "Copy Rollout Air Speed", 1)
kirby.add_attribute(attribute_data, 0x344, "Copy Rollout Turn Rate Variable", 1)
kirby.add_attribute(attribute_data, 0x358, "Copy Rollout Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x35C, "Copy Shield Breaker Loops For Full Charge", 1)
kirby.get_attribute("Copy Shield Breaker Loops For Full Charge").integer = True
kirby.add_attribute(attribute_data, 0x360, "Copy Shield Breaker Base Damage", 1)
kirby.get_attribute("Copy Shield Breaker Base Damage").integer = True
kirby.add_attribute(attribute_data, 0x364, "Copy Shield Breaker Damage Per Loop", 1)
kirby.get_attribute("Copy Shield Breaker Damage Per Loop").integer = True
kirby.add_attribute(attribute_data, 0x36C, "Copy Shield Breaker Momentum Preservation", 1)
kirby.add_attribute(attribute_data, 0x36C, "Copy Shield Breaker Deceleration Rate", 1)
kirby.add_attribute(attribute_data, 0x370, "Copy Flare Blade Loops For Full Charge", 1)
kirby.get_attribute("Copy Flare Blade Loops For Full Charge").integer = True
kirby.add_attribute(attribute_data, 0x374, "Copy Flare Blade Base Damage", 1)
kirby.get_attribute("Copy Flare Blade Base Damage").integer = True
kirby.add_attribute(attribute_data, 0x378, "Copy Flare Blade Damage Per Loop", 1)
kirby.get_attribute("Copy Flare Blade Damage Per Loop").integer = True
kirby.add_attribute(attribute_data, 0x37C, "Copy Flare Blade Momentum Preservation", 1)
kirby.add_attribute(attribute_data, 0x380, "Copy Flare Blade Deceleration Rate", 1)
kirby.add_attribute(attribute_data, 0x384, "Copy Shadow Ball Charge Increment", 1)
kirby.add_attribute(attribute_data, 0x388, "Copy Shadow Ball Release Momentum Grounded", 1)
kirby.add_attribute(attribute_data, 0x38C, "Copy Shadow Ball Release Momentum Air", 1)
kirby.add_attribute(attribute_data, 0x390, "Copy Shadow Ball Loops For Full Charge", 1)
kirby.get_attribute("Copy Shadow Ball Loops For Full Charge").integer = True
kirby.add_attribute(attribute_data, 0x398, "Copy Shadow Ball Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x39C, "Copy Ice Shot Aerial Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0x3A0, "Copy Ice Shot Landing Lag", 1)
kirby.add_attribute(attribute_data, 0x3A4, "Copy Ice Shot Spawn X-Offset", 1)
kirby.add_attribute(attribute_data, 0x3A8, "Copy Ice Shot Spawn Y-Offset", 1)
kirby.add_attribute(attribute_data, 0x3AC, "Copy Egg Lay Horizontal Momentum", 1)
kirby.add_attribute(attribute_data, 0x3B0, "Copy Egg Lay Vertical Momentum", 1)
kirby.add_attribute(attribute_data, 0x3B4, "Copy Egg Lay Damage Multiplier", 1)
kirby.add_attribute(attribute_data, 0x3BC, "Copy Egg Lay Growth Time", 1)
kirby.add_attribute(attribute_data, 0x3C0, "Copy Egg Lay Base Duration", 1)
kirby.add_attribute(attribute_data, 0x3C4, "Copy Egg Lay Breakout Resistance", 1)
kirby.add_attribute(attribute_data, 0x3C8, "Copy Egg Lay Wiggle Out", 1)
kirby.add_attribute(attribute_data, 0x3D4, "Copy Egg Lay Release Intangibility", 1)
kirby.get_attribute("Copy Egg Lay Release Intangibility").integer = True
kirby.add_attribute(attribute_data, 0x3D8, "Copy Egg Lay Break Out Horizontal Velocity", 1)
kirby.add_attribute(attribute_data, 0x3DC, "Copy Egg Lay Break Out Vertical Velocity", 1)
kirby.add_attribute(attribute_data, 0x3E4, "Copy Chef Multi Hit Begin Frame", 1)
kirby.add_attribute(attribute_data, 0x3E8, "Copy Chef Max Sausages", 1)

kirby.article_datas = kirby.dat_file.get_article_data(kirby)
final_cutter_data = kirby.article_datas[0]
kirby.add_attribute(final_cutter_data, 0x0, "Final Cutter Velocity", 2)
kirby.add_attribute(final_cutter_data, 0x8, "Final Cutter Duration", 2)
kirby.add_attribute(final_cutter_data, 0xC, "Final Cutter Deceleration Rate", 2)