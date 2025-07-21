import fighter
from iso import DAT
from structs import hitbox

sheik = fighter.Fighter("Sheik", DAT(b'PlSk.dat'))
fighter.fighters.append(sheik)
sheik.fighter_id = 0x13

sheik.special_attribute_block_size = 0x74
sheik.articles_sizes = [0xC, 0x6C]
sheik.articles_offsets = [0x3994, 0x3C1C]
sheik.projectile_offsets = [0x39C0]

file_data = sheik.dat_file.file_data
offset = sheik.projectile_offsets[0]
needle_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
needle_hitbox.tags.append("projectile")
sheik.projectile_hitboxes.append(needle_hitbox)

sheik.subactions[303].friendly_name = "Chain Dance"

attribute_data = sheik.dat_file.get_special_attribute_data(sheik.special_attribute_block_size)
sheik.add_attribute(attribute_data, 0x14, "Chain Dance Base Duration", 1)
sheik.add_attribute(attribute_data, 0x18, "Chain Dance Rehit Rate", 1)
sheik.add_attribute(attribute_data, 0x20, "Chain Dance Control Frame", 1)
sheik.add_attribute(attribute_data, 0x24, "Chain Dance Retraction Delay Frame", 1)
sheik.add_attribute(attribute_data, 0x28, "Chain Dance Retraction Begin Frame", 1)
sheik.add_attribute(attribute_data, 0x2C, "Vanish Vertical Momentum", 1)
sheik.add_attribute(attribute_data, 0x30, "Vanish Physics Variable", 1)
sheik.add_attribute(attribute_data, 0x34, "Vanish Fall Acceleration", 1)
sheik.add_attribute(attribute_data, 0x38, "Vanish Travel Distance", 1)
sheik.get_attribute("Vanish Travel Distance").integer = True
sheik.add_attribute(attribute_data, 0x44, "Vanish Base Momentum", 1)
sheik.add_attribute(attribute_data, 0x48, "Vanish Momentum Variable", 1)
sheik.add_attribute(attribute_data, 0x4C, "Vanish Momentum After Poof", 1)
sheik.add_attribute(attribute_data, 0x54, "Vanish Momentum After Poof 2", 1)
sheik.add_attribute(attribute_data, 0x5C, "Vanish Landing Lag", 1)
sheik.add_attribute(attribute_data, 0x60, "Transform Horizontal Momentum Preservation", 1)
sheik.add_attribute(attribute_data, 0x64, "Transform Vertical Momentum Preservation", 1)

sheik.article_datas = sheik.dat_file.get_article_data(sheik)
needle_data = sheik.article_datas[0]
sheik.add_attribute(needle_data, 0x0, "Needles Air Duration", 2)
sheik.add_attribute(needle_data, 0x4, "Needles Ground Duration", 2)
sheik.add_attribute(needle_data, 0x8, "Needles Travel Speed", 2)

chain_data = sheik.article_datas[1]
sheik.add_attribute(chain_data, 0x0, "Chain Number of Segments", 2)
sheik.get_attribute("Chain Number of Segments").integer = True
sheik.add_attribute(chain_data, 0x4, "Chain Size", 2)
sheik.add_attribute(chain_data, 0x10, "Chain Gravity/Elasticity", 2)
sheik.add_attribute(chain_data, 0x14, "Chain Collision Sensitivity", 2)
sheik.add_attribute(chain_data, 0x18, "Chain Gravity Modifier", 2)
sheik.add_attribute(chain_data, 0x1C, "Chain Rebound Sensitivity", 2)
sheik.add_attribute(chain_data, 0x20, "Chain Movement Modifier 2", 2)
sheik.add_attribute(chain_data, 0x24, "Chain Mystery Value 1", 2)
sheik.add_attribute(chain_data, 0x28, "Chain Mystery Value 2", 2)
sheik.add_attribute(chain_data, 0x2C, "Chain Mystery Value 3", 2)
sheik.add_attribute(chain_data, 0x30, "Chain Mystery Value 4", 2)
sheik.add_attribute(chain_data, 0x34, "Chain Falling Speed", 2)
sheik.add_attribute(chain_data, 0x38, "Chain Rebound Modifier 1", 2)
sheik.add_attribute(chain_data, 0x3C, "Chain Rebound Modifier 2", 2)
sheik.add_attribute(chain_data, 0x40, "Chain Delay Before Fall Acceleration", 2)
sheik.add_attribute(chain_data, 0x44, "Chain Falling Mod", 2)
sheik.add_attribute(chain_data, 0x48, "Chain Movement Modifier 2", 2)
sheik.add_attribute(chain_data, 0x50, "Chain Spawn Position", 2)
sheik.add_attribute(chain_data, 0x54, "Chain Movement Modifier 3", 2)
sheik.add_attribute(chain_data, 0x58, "Chain Movement Modifier 4", 2)
sheik.add_attribute(chain_data, 0x5C, "Chain Rebound from Collision", 2)
sheik.add_attribute(chain_data, 0x60, "Chain Movement Modifier 5", 2)