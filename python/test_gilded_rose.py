# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_normal_item(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[0].sell_in, 9)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[0].sell_in, 9)

    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[0].sell_in, 10)
        
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 23)
        self.assertEqual(items[0].sell_in, 9)
        
        items[0].sell_in = 5
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 26)
        self.assertEqual(items[0].sell_in, 4)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 10)

    def test_conjured_items(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)
        self.assertEqual(items[0].sell_in, 2)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 2)
        self.assertEqual(items[0].sell_in, 1)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, 0)

if __name__ == '__main__':
    unittest.main()
