#!/usr/bin/env python3

from random import randrange

__all__ = ['vocabulary']

chapter1Words = [
    { 'word': 'あの', 'definition': 'um...'},
    { 'word': 'いま', 'definition': 'now'},
    { 'word': 'えいご', 'definition': 'English (language)'},
    { 'word': 'ええ', 'definition': 'yes'},
    { 'word': 'がくせい', 'definition': 'student'},
    { 'word': '〜ご', 'definition': '...language (ex: えいご)'},
    { 'word': 'こうこう', 'definition': 'high school'},
    { 'word': 'ごご', 'definition': 'P.M.'},
    { 'word': 'ごぜん', 'definition': 'A.M.'},
    { 'word': '〜さい', 'definition': 'X Years Old (ex: 一さい)'},
    { 'word': '〜さん', 'definition': 'Mr./Ms.'},
    { 'word': '〜じ', 'definition': 'o\'clock (ex: 二十じ)'},
    { 'word': '〜じん', 'definition': '...person (ex: にほんじん)'},
    { 'word': 'せんこう', 'definition': 'major'},
    { 'word': 'せんせい', 'definition': 'teacher; professor'},
    { 'word': 'そうです', 'definition': 'that\'s right'},
    { 'word': 'そうですか', 'definition': 'I see.; Is that so?'},
    { 'word': 'だいがく', 'definition': 'college; university'},
    { 'word': 'でんわ', 'definition': 'telephone'},
    { 'word': 'ともだち', 'definition': 'friend'},
    { 'word': 'なまえ', 'definition': 'name'},
    { 'word': 'なん/なに', 'definition': 'what'},
    { 'word': 'にほん', 'definition': 'Japan'},
    { 'word': '〜ねんせい', 'definition': 'X year student (ex: 二ねんせい)'},
    { 'word': 'はい', 'definition': 'yes'},
    { 'word': 'はん', 'definition': 'half (ex: 一じはん)'},
    { 'word': 'ばんごう', 'definition': 'number'},
    { 'word': 'りゅうがくせい', 'definition': 'international student'},
    { 'word': 'わたし', 'definition': 'I'},
    { 'word': 'アメリカ', 'definition': 'U.S.A'},
    { 'word': 'イギリス', 'definition': 'Britain'},
    { 'word': 'オーストラリア', 'definition': 'Australia'},
    { 'word': 'かんこく', 'definition': 'Korea'},
    { 'word': 'スウェーデん', 'definition': 'Sweden'},
    { 'word': 'ちゅうごく', 'definition': 'China'},
    { 'word': 'かがく', 'definition': 'science'},
    { 'word': 'アジアけんきゅう', 'definition': 'asian studies'},
    { 'word': 'こくさいかんけい', 'definition': 'international relations'},
    { 'word': 'コンピューター', 'definition': 'computer'},
    { 'word': 'じんるいがく', 'definition': 'anthropology'},
    { 'word': 'せいじ', 'definition': 'politics'},
    { 'word': 'ビジネス', 'definition': 'business'},
    { 'word': 'れきし', 'definition': 'history'},
    { 'word': 'しごと', 'definition': 'job;; work; occupation'},
    { 'word': 'いしゃ', 'definition': 'doctor'},
    { 'word': 'かいしゃいん', 'definition': 'office worker'},
    { 'word': 'こうこうせい', 'definition': 'high school student'},
    { 'word': 'しゅふ', 'definition': 'housewife'},
    { 'word': 'だいがくいんせい', 'definition': 'graduate student'},
    { 'word': 'だいがくせい', 'definition': 'college student'},
    { 'word': 'べんごし', 'definition': 'lawyar'},
    { 'word': 'おかあさん', 'definition': 'mother'},
    { 'word': 'おとうさん', 'definition': 'father'},
    { 'word': 'おねえさん', 'definition': 'older sister'},
    { 'word': 'おにいさん', 'definition': 'older brother'},
    { 'word': 'いもうと', 'definition': 'younger sister'},
    { 'word': 'おとうと', 'definition': 'younger brother'}
]

chapter2Words = [
    { 'word': 'これ', 'definition': 'this one'},
    { 'word': 'それ', 'definition': 'that one'},
    { 'word': 'あれ', 'definition': 'that one (over there)'},
    { 'word': 'どれ', 'definition': 'which one'},
    { 'word': 'この', 'definition': 'this...'},
    { 'word': 'その', 'definition': 'that...'},
    { 'word': 'あの', 'definition': 'that... (over there)'},
    { 'word': 'どの', 'definition': 'which...'},
    { 'word': 'ここ', 'definition': 'here'},
    { 'word': 'そこ', 'definition': 'there'},
    { 'word': 'あそこ', 'definition': 'over there'},
    { 'word': 'どこ', 'definition': 'where'},
    { 'word': 'だれ', 'definition': 'who'},
    { 'word': 'おいしい', 'definition': 'delicious'},
    { 'word': 'さかな', 'definition': 'fish'},
    { 'word': 'とんかつ', 'definition': 'pork cutlet'},
    { 'word': 'にく', 'definition': 'meat'},
    { 'word': 'メニュー', 'definition': 'menu'},
    { 'word': 'やさい', 'definition': 'vegetable'},
    { 'word': 'えんぴつ', 'definition': 'pencil'},
    { 'word': 'かさ', 'definition': 'umbrella'},
    { 'word': 'かばん', 'definition': 'bag'},
    { 'word': 'くつ', 'definition': 'shoes'},
    { 'word': 'さいふ', 'definition': 'wallet'},
    { 'word': 'ジーンズ', 'definition': 'jeans'},
    { 'word': 'じしょ', 'definition': 'dictionary'},
    { 'word': 'じてんしゃ', 'definition': 'bicycle'},
    { 'word': 'しんぶん', 'definition': 'newspaper'},
    { 'word': 'Tシャツ', 'definition': 'T-shirt'},
    { 'word': 'とけい', 'definition': 'watch; clock'},
    { 'word': 'ノート', 'definition': 'notebook'},
    { 'word': 'ペン', 'definition': 'pen'},
    { 'word': 'ほうし', 'definition': 'hat; cap'},
    { 'word': 'ほん', 'definition': 'book'},
    { 'word': 'きっさてん', 'definition': 'cafe'},
    { 'word': 'ぎんこう', 'definition': 'bank'},
    { 'word': 'トイレ', 'definition': 'toilet; restroom'},
    { 'word': 'としょかん', 'definition': 'library'},
    { 'word': 'ゆうびんきょく', 'definition': 'post office'},
    { 'word': 'けいざい', 'definition': 'economics'},
    { 'word': 'いくら', 'definition': 'how much'},
    { 'word': '〜えん', 'definition': '... yen (ex: 三千円・三千えん)'},
    { 'word': 'たかい', 'definition': 'expensive; high'},
    { 'word': 'いらっしゃいませ', 'definition': 'Welcome (to our store)'},
    { 'word': '（〜を）おねがいします', 'definition': '... please'},
    { 'word': '（〜を）ください', 'definition': 'Please give me...'},
    { 'word': 'じゃあ', 'definition': 'then...; if that\'s the case...'},
    { 'word': 'どうぞ', 'definition': 'please.; here it is.'},
    { 'word': 'どうも', 'definition': 'thank you.'}
]

chapter3Words = [
    { 'word': 'えいが', 'definition': 'movie', 'type': 'noun'},
    { 'word': '映画', 'definition': 'movie', 'reading': 'えいが', 'type': 'noun'},
    { 'word': 'おんがく', 'definition': 'music', 'type': 'noun'},
    { 'word': '音楽', 'definition': 'music', 'reading': 'おんがく', 'type': 'noun'},
    { 'word': 'ざっし', 'definition': 'magazine', 'type': 'noun'},
    { 'word': '雑誌', 'definition': 'magazine', 'reading': 'ざっし', 'type': 'noun'},
    { 'word': 'スポーツ', 'definition': 'sports', 'type': 'noun'},
    { 'word': 'デート', 'definition': 'date (romantic, not calendar)', 'type': 'noun'},
    { 'word': 'テニス', 'definition': 'tennis', 'type': 'noun'},
    { 'word': 'テレビ', 'definition': 'TV', 'type': 'noun'},
    { 'word': 'アイスクリーム', 'definition': 'ice cream', 'type': 'noun'},
    { 'word': 'おさごはん', 'definition': 'breakfast', 'type': 'noun'},
    { 'word': '朝ご飯', 'definition': 'breakfast', 'reading': 'おさごはん', 'type': 'noun'},
    { 'word': 'おさけ', 'definition': 'sake; alcohol', 'type': 'noun'},
    { 'word': 'お酒', 'definition': 'sake; alcohol', 'reading': 'おさけ', 'type': 'noun'},
    { 'word': 'おちゃ', 'definition': 'green tea', 'type': 'noun'},
    { 'word': 'お茶', 'definition': 'green tea', 'reading': 'おちゃ', 'type': 'noun'},
    { 'word': 'コーヒー', 'definition': 'coffee', 'type': 'noun'},
    { 'word': 'ばんごはん', 'definition': 'dinner', 'type': 'noun'},
    { 'word': '晩ご飯', 'definition': 'dinner', 'reading': 'ばんごはん', 'type': 'noun'},
    { 'word': 'ハンバーガー', 'definition': 'hamburger', 'type': 'noun'},
    { 'word': 'ひるごはん', 'definition': 'lunch', 'type': 'noun'},
    { 'word': '昼ご飯', 'definition': 'lunch', 'reading': 'ひるごはん', 'type': 'noun'},
    { 'word': 'みず', 'definition': 'water', 'type': 'noun'},
    { 'word': '水', 'definition': 'water', 'reading': 'みず', 'type': 'noun'},
    { 'word': 'いえ', 'definition': 'home; house', 'type': 'noun'},
    { 'word': '家', 'definition': 'home; house', 'reading': 'いえ', 'type': 'noun'},
    { 'word': 'うち', 'definition': 'home; house; my place', 'type': 'noun'},
    { 'word': 'がっこう', 'definition': 'school', 'type': 'noun'},
    { 'word': '学校', 'definition': 'school', 'reading': 'がっこう', 'type': 'noun'},
    { 'word': 'いく', 'definition': 'to go (destination に・へ)', 'type': 'U-verb'},
    { 'word': '行く', 'definition': 'to go (destination に・へ)', 'reading': 'いく', 'type': 'U-verb'},
    { 'word': 'かえる', 'definition': 'to go back; to return (destination に・へ)', 'type': 'U-verb'},
    { 'word': '帰る', 'definition': 'to go back; to return (destination に・へ)', 'reading': 'かえる', 'type': 'U-verb'},
    { 'word': 'きく', 'definition': 'to listen; to hear (〜を)', 'type': 'U-verb'},
    { 'word': '聞く', 'definition': 'to listen; to hear (〜を)', 'reading': 'きく', 'type': 'U-verb'},
    { 'word': 'のむ', 'definition': 'to drink (〜を)', 'type': 'U-verb'},
    { 'word': '飲む', 'definition': 'to drink (〜を)', 'reading': 'のむ', 'type': 'U-verb'},
    { 'word': 'はなす', 'definition': 'to speak; to talk (language を・で)', 'type': 'U-verb'},
    { 'word': '話す', 'definition': 'to speak; to talk', 'reading': 'はなす', 'type': 'U-verb'},
    { 'word': 'よむ', 'definition': 'to read (〜を)', 'type': 'U-verb'},
    { 'word': '読む', 'definition': 'to read (〜を)', 'reading': 'よむ', 'type': 'U-verb'},
    { 'word': 'おきる', 'definition': 'to get up', 'type': 'Ru-verb'},
    { 'word': '起きる', 'definition': 'to get up', 'reading': 'おきる', 'type': 'Ru-verb'},
    { 'word': 'たべる', 'definition': 'to eat (〜を)', 'type': 'Ru-verb'},
    { 'word': '食べる', 'definition': 'to eat (〜を)', 'reading': 'たべる', 'type': 'Ru-verb'},
    { 'word': 'ねる', 'definition': 'to sleep; go to sleep', 'type': 'Ru-verb'},
    { 'word': '寝る', 'definition': 'to sleep; go to sleep', 'reading': 'ねる', 'type': 'Ru-verb'},
    { 'word': 'みる', 'definition': 'to see; to look at (〜を); to watch', 'type': 'Ru-verb'},
    { 'word': '見る', 'definition': 'to see; to look at (〜を)', 'reading': 'みる', 'type': 'Ru-verb'},
    { 'word': 'くる', 'definition': 'to come (destination に・へ)', 'type': 'Irregular verb'},
    { 'word': '来る', 'definition': 'to come (destination に・へ)', 'reading': 'くる', 'type': 'Irregular verb'},
    { 'word': 'する', 'definition': 'to do (〜を)', 'type': 'Irregular verb'},
    { 'word': 'べんきょうする', 'definition': 'to study (〜を)', 'type': 'Irregular verb'},
    { 'word': '勉強する', 'definition': 'to study (〜を)', 'reading': 'べんきょうする', 'type': 'Irregular verb'},
    { 'word': 'いい', 'definition': 'good', 'type': 'adjective'},
    { 'word': 'はやい', 'definition': 'early', 'type': 'adjective'},
    { 'word': '早い', 'definition': 'def', 'reading': 'はやい', 'type': 'adjective'},
    { 'word': 'あまる＋negative', 'definition': 'not much', 'type': 'adverb'},
    { 'word': 'ぜんぜん＋negative', 'definition': 'not at all', 'type': 'adverb'},
    { 'word': '全然', 'definition': 'not at all', 'reading': 'ぜんぜん＋negative', 'type': 'adverb'},
    { 'word': 'たいてい', 'definition': 'usually', 'type': 'adverb'},
    { 'word': 'ちょっと', 'definition': 'a little', 'type': 'adverb'},
    { 'word': 'ときどき', 'definition': 'sometimes', 'type': 'adverb'},
    { 'word': '時々', 'definition': 'sometimes', 'reading': 'ときどき', 'type': 'adverb'},
    { 'word': 'よく', 'definition': 'often; much', 'type': 'adverb'},
    { 'word': 'そうですね', 'definition': 'That\'s right; Let me see.', 'type': 'Expression'},
    { 'word': 'でも', 'definition': 'but', 'type': 'Expression'},
    { 'word': 'どうですか', 'definition': 'How about...?; How is...?', 'type': 'Expression'}
]

vocabulary = chapter1Words + chapter2Words + chapter3Words