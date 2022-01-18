import unittest

from bs4 import BeautifulSoup

from grim_calc.utils.rip_items_from_grimtools.item_list_to_sqlite import (
    Item,
    parse_item,
    OneHandedSword,
    Damage,
)


class MyTestCase(unittest.TestCase):
    def test_parse_item_gives_sword(self):
        example_div = """<div class="item-card item-weapon" item-id="it2724">
    <div class="item-bitmap-container">
        <div class="item-bitmap-background bg-common"></div>
        <div class="item-bitmap itemdb itemdb-items_gearweapons_swords1h_bitmaps_a02_sword002"></div>
    </div>
    <div class="item-description">
        <div><a class="item-name common" item-id="it2724">Tarnished Carver</a></div>
        <div class="item-type">One-Handed Sword</div>
        <div class="item-base-stats">
            <div>12-34 <span class="text-silver">Physical Damage</span></div>
            <div>10% <span class="text-silver">Armor Piercing</span></div>
            <div><span class="text-white">1.88 </span><span class="text-silver">Attacks per Second</span></div>
        </div>
        <div class="item-req">
            <div>Required Cunning: 83</div>
            <div>Item Level: 8</div>
        </div>
    </div>
</div>"""
        example_tag = BeautifulSoup(example_div, "html.parser")
        damage = Damage(12, 34, "Physical", False)
        expected_item = OneHandedSword("common", "Tarnished Carver", 1.88, [damage])
        actual_item = parse_item(example_tag)
        assert expected_item == actual_item


if __name__ == "__main__":
    unittest.main()
