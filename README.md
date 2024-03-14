# speechToTextFaster

using repo `https://pypi.org/project/faster-whisper/`

## Setup

install using `pip install -r requirements.txt`

## Run

`python speechToTextFaster.py`

# speechToTextTimestamped

using repo `https://github.com/linto-ai/whisper-timestamped`

## Setup

install using `pip install -r requirements.txt`

## Run

`python speechToTextTimestamped.py`

# RESULTS

## speechToTextFaster

(after first run, so cached the Large LM already)

```
$ time python speechToTextFaster.py 
Detected language 'en' with probability 0.999803
[0.00s -> 4.40s]  Unfolding Word, Open Bible Stories
[4.40s -> 8.30s]  Story 1. The Creation
[8.30s -> 12.12s]  This is how God made everything in the beginning.
[13.06s -> 17.06s]  He created the universe and everything in it in six days.
[17.54s -> 24.60s]  After God created the earth, it was dark and empty because He had not yet formed anything in it.
[25.32s -> 28.04s]  But God's Spirit was there over the water.
[28.04s -> 30.04s]  Then God said,
[30.66s -> 45.68s]  God created the light on the first day of creation.
[46.56s -> 49.36s]  On the second day of creation, God said,
[49.36s -> 52.12s]  Let there be an expanse above the waters.
[52.76s -> 54.26s]  And there was an expanse.
[55.00s -> 57.44s]  God called this expanse sky.
[58.04s -> 60.46s]  On the third day, God said,
[60.46s -> 65.06s]  Let the water come together in one place, and the dry land appear.
[65.90s -> 69.78s]  He called the dry land earth, and He called the water seas.
[70.52s -> 73.40s]  God saw that what He had created was good.
[74.46s -> 75.40s]  Then God said,
[76.06s -> 79.22s]  Let the earth produce all kinds of trees and plants.
[79.84s -> 81.08s]  And that is what happened.
[81.84s -> 84.90s]  God saw that what He had created was good.
[85.68s -> 87.46s]  On the fourth day of creation,
[88.08s -> 88.74s]  God said,
[89.44s -> 91.14s]  Let there be lights in the sky.
[91.76s -> 94.74s]  And the sun, the moon, and the stars appeared.
[95.54s -> 101.48s]  God made them to give light to the earth and to mark day and night, seasons and years.
[102.24s -> 105.24s]  God saw that what He had created was good.
[105.88s -> 108.26s]  On the fifth day, God said,
[108.26s -> 113.30s]  Let living things fill the waters, and birds fly in the sky.
[114.04s -> 117.26s]  This is how He made everything that swims in the water and all.
[117.46s -> 121.88s]  God saw that it was good, and He blessed them.
[122.48s -> 125.60s]  On the sixth day of creation, God said,
[126.20s -> 128.38s]  Let there be all kinds of land animals.
[129.18s -> 131.24s]  And it happened just like God said.
[131.92s -> 136.88s]  Some were farm animals, some crawled on the ground, and some were wild.
[137.66s -> 139.40s]  And God saw that it was good.
[140.32s -> 141.28s]  Then God said,
[141.84s -> 145.68s]  Let us make human beings in our image to be like us.
[145.98s -> 147.36s]  They will rule over the earth.
[147.36s -> 149.36s]  They will rule over the earth, and all the animals.
[150.22s -> 155.44s]  So God took some soil, formed it into a man, and breathed life into him.
[156.14s -> 157.86s]  This man's name was Adam.
[158.58s -> 163.48s]  God planted a large garden where Adam could live, and put him there to care for it.
[164.22s -> 167.82s]  In the middle of the garden, God planted two special trees,
[168.40s -> 172.18s]  the tree of life and the tree of the knowledge of good and evil.
[172.66s -> 175.80s]  God told Adam that he could eat from any tree in the garden,
[176.04s -> 177.34s]  except from the tree of the knowledge.
[177.36s -> 178.76s]  The tree of life and the tree of the knowledge of good and evil.
[179.30s -> 182.44s]  If he ate from this tree, he would die.
[183.38s -> 184.30s]  Then God said,
[185.00s -> 187.22s]  It is not good for man to be alone,
[187.74s -> 190.20s]  but none of the animals could be Adam's helper.
[191.04s -> 193.74s]  So God made Adam fall into a deep sleep.
[194.46s -> 199.68s]  Then God took one of Adam's ribs and made it into a woman and brought her to him.
[200.38s -> 202.44s]  When Adam saw her, he said,
[202.90s -> 205.46s]  At last, this one is like me.
[205.74s -> 207.32s]  Let her be called woman,
[207.36s -> 209.38s]  for she was made from man.
[210.08s -> 214.76s]  This is why a man leaves his father and mother and becomes one with his wife.
[215.78s -> 218.66s]  God made man and woman in his own image.
[219.40s -> 221.04s]  He blessed them and told them,
[221.64s -> 225.06s]  Have many children and grandchildren, and fill the earth.
[225.90s -> 228.98s]  And God saw that everything he had made was very good,
[229.38s -> 231.68s]  and he was very pleased with all of it.
[232.30s -> 235.40s]  This all happened on the sixth day of creation.
[235.94s -> 237.34s]  When the seventh day came,
[237.90s -> 240.70s]  God had finished all the work that he had been doing.
[241.28s -> 243.96s]  He blessed the seventh day and made it holy,
[244.50s -> 247.40s]  because on this day he stopped creating things.
[248.08s -> 252.56s]  This is how God created the universe and everything in it.
[253.58s -> 258.24s]  A Bible story from the book of Genesis, chapters 1 and 2.

real    5m9.525s
user    16m24.123s
sys     2m29.892s
```

## spechToTextTimestamped

(after first run, so cached the Timestamped Tiny LM already)

```
$ time python speechToTextTimestam
ped.py 
Detected language: English
100%|█████████████████████████████████████████████████████████████████████| 26000/26000 [00:30<00:00, 865.72frames/s]
Detected language 'en' with probability 0.995509
[1.32s -> 4.54s]  Unfolding word, open Bible stories.
[6.20s -> 8.46s]  Story one, the creation.
[9.66s -> 12.32s]  This is how God made everything in the beginning.
[13.02s -> 17.26s]  He created the universe in everything in it in six days.
[18.02s -> 24.02s]  After God created the earth, it was dark and empty because he had not yet formed anything
[24.02s -> 24.86s]  in it.
[25.30s -> 28.24s]  But God's spirit was there over the water.
[29.20s -> 33.60s]  And God said, let there be light and there was light.
[34.28s -> 37.48s]  God saw that the light was good and called it day.
[38.04s -> 41.84s]  He separated it from the darkness, which he called night.
[42.48s -> 45.80s]  God created the light on the first day of creation.
[46.58s -> 52.26s]  On the second day of creation, God said, let there be an expanse above the waters.
[52.72s -> 54.52s]  And there was an expanse.
[55.32s -> 57.58s]  God called this expanse, sky.
[58.40s -> 64.68s]  On the third day, God said, let the water come together in one place in the dry land
[64.68s -> 65.22s]  appear.
[65.94s -> 69.96s]  He called the dry land earth and he called the water seize.
[70.54s -> 73.68s]  God saw that what he had created was good.
[74.50s -> 79.36s]  Then God said, let the earth produce all kinds of trees and plants.
[79.86s -> 81.20s]  And that is what happened.
[82.12s -> 85.08s]  God saw that what he had created was good.
[86.02s -> 92.64s]  On the fourth day of creation, God said, let there be lights in the sky and the sun,
[92.80s -> 94.90s]  the moon and the stars appeared.
[95.60s -> 101.82s]  God made them to give light to the earth and to mark day and night, seasons and years.
[102.34s -> 105.46s]  God saw that what he had created was good.
[106.36s -> 113.46s]  On the fifth day, God said, let living things fill the waters and birds fly in the sky.
[113.88s -> 118.30s]  This is how he made everything that swims in the water and all the birds.
[119.02s -> 122.18s]  God saw that it was good and he blessed them.
[122.76s -> 128.56s]  On the sixth day of creation, God said, let there be all kinds of land animals.
[129.16s -> 131.56s]  And it happened just like God said.
[132.16s -> 137.08s]  One more farm animals, some crawled on the ground and some were wild.
[137.68s -> 139.64s]  In God saw that it was good.
[140.38s -> 145.90s]  Then God said, let us make human beings in our image to be like us.
[146.42s -> 149.44s]  They will rule over the earth and all the animals.
[150.26s -> 155.82s]  So God took some soil, formed it into a man and breathed life into him.
[156.26s -> 158.20s]  This man's name was Adam.
[158.84s -> 163.74s]  God planted a large garden where Adam could live and put him there to care for it.
[164.24s -> 170.20s]  In the middle of the garden, God planted two special trees, the tree of life and the tree
[170.20s -> 172.40s]  of the knowledge of good and evil.
[172.98s -> 177.30s]  God told Adam that he could eat from any tree in the garden except from the tree of
[177.30s -> 178.90s]  the knowledge of good and evil.
[179.58s -> 182.66s]  If he ate from this tree, he would die.
[183.38s -> 187.34s]  Then God said, it is not good for man to be alone.
[188.04s -> 190.44s]  But none of the animals could be Adam's helper.
[191.16s -> 193.80s]  So God made Adam fall into a deep sleep.
[194.44s -> 200.12s]  Then God took one of Adam's ribs and made it into a woman and brought her to him.
[200.44s -> 205.94s]  When Adam saw her, he said, at last, this one is like me.
[206.18s -> 209.64s]  Let her be called woman for she was made from man.
[210.20s -> 214.96s]  This is why a man leaves his father and mother and becomes one with his wife.
[216.04s -> 218.78s]  God made man and woman in his own image.
[219.38s -> 225.30s]  He blessed them and told them, have many children and grandchildren and fill the earth.
[225.94s -> 231.33s]  And God saw that everything he had made was very good and he was very pleased with all
[231.33s -> 232.20s]  of it.
[232.54s -> 235.54s]  This all happened on the sixth day of creation.
[236.38s -> 240.84s]  When the seventh day came, God had finished all the work that he had been doing.
[241.56s -> 247.58s]  He blessed the seventh day and made it holy because on this day he stopped creating things.
[248.38s -> 253.16s]  This is how God created the universe and everything in it.
[254.02s -> 258.30s]  A Bible story from the Book of Genesis 1 and 2.

real    0m35.890s
user    1m30.592s
sys     0m48.356s
```