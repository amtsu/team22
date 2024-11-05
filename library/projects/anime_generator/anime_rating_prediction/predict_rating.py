# Импорт нужных библиотек
import torch
from transformers import BertTokenizer, BertModel, BertConfig
import logging
import os

# Загрузка токенизатора BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


# Загрузка сохраненной модели
class BertForRegression(torch.nn.Module):
    def __init__(self, bert):
        super(BertForRegression, self).__init__()
        self.bert = bert
        self.regressor = torch.nn.Linear(bert.config.hidden_size, 1)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        cls_output = outputs.pooler_output
        rating = self.regressor(cls_output)
        return rating


# Настройка модели BERT для регрессии
config = BertConfig.from_pretrained('bert-base-uncased', num_labels=1)

# Проверка наличия предобученной модели на диске
model_path = 'bert_model'
if os.path.exists(model_path):
    logging.info("Загрузка предобученной BERT-модели из локального файла")
    bert_model = BertModel.from_pretrained(model_path)
else:
    logging.info("Загрузка предобученной BERT-модели с сервера и сохранение на диск с выводом прогресса")
    config = BertConfig.from_pretrained('bert-base-uncased', num_labels=1)
    bert_model = BertModel.from_pretrained('bert-base-uncased', config=config)
    bert_model.save_pretrained(model_path)

# Инициализация модели
model = BertForRegression(bert_model)

# Загрузка весов модели
model.load_state_dict(torch.load('bert_rating_model.pth'))

# Перевод модели в режим оценки (инференса)
model.eval()

origin = (['chat gpt 4o'] * 7) + (['llama 7b'] * 7) + (['gemma 2 27b'] * 5) + (['mistral small 21b'] * 8)

new_reviews = [
    # chat gpt
    "In a world where magic is fading, a young mage named Lyra discovers a relic that grants her the ability to communicate with celestial beings. Along with an exiled knight and a mysterious thief, she embarks on a journey across the Astral Sea to restore magic. But the forces that drained the world of its power won't let her succeed without a fight, as dark gods and ancient creatures rise to stop her.",
    "In the year 2215, Earth is on the brink of destruction due to an alien invasion. Humanity’s only hope lies in massive, sentient mechs known as \"Titans,\" relics from an ancient civilization. Kazuto, a rebellious teenager, unexpectedly bonds with one of the Titans, gaining the power to lead humanity's counterattack. As he learns the truth about the Titans and the aliens, Kazuto must decide whether to follow orders or trust his own instincts to save the planet.",
    "Akira is an ordinary high school student with an extraordinary problem—his next-door neighbor, Yumi, is secretly a ninja in training. Tasked with observing Akira for her clan’s covert mission, Yumi's lack of people skills leads to hilarious misunderstandings. As Akira tries to balance his normal life with Yumi’s antics, sparks fly in the most unexpected ways. Will their budding romance survive hidden weapons, sudden rooftop battles, and high school exams?",
    "In the small town of Mizuhara, people start disappearing under mysterious circumstances every month. The only clue left behind are red lanterns glowing in the forest. Four high school friends decide to investigate, uncovering a hidden world of ancient spirits and cursed rituals. As they delve deeper, they must confront their darkest fears or risk becoming the next victims of the lantern’s curse. Can they break the cycle before it's too late?",
    "Hinata, a college student struggling with the recent death of her mother, moves to a small coastal town for a fresh start. There, she meets a group of locals, each dealing with their own personal struggles. Through shared moments, from rainy afternoons to summer festivals, Hinata begins to heal and form deep connections. \"After the Rain\" explores themes of grief, friendship, and the slow, sometimes painful process of moving forward.",
    "Tatsuya was once a rising basketball star, but after an injury, he gave up on his dreams. However, when a street basketball team known for its intense underground matches challenges him, Tatsuya is pulled back into the game. With nothing to lose, he joins the team, determined to rise to the top of the streetball world. With fierce rivals, creative strategies, and breathtaking plays, \"Blazing Court\" is a high-stakes sports anime about redemption and the love of the game.",
    "Detective Haruto Aizawa is known for his sharp mind and flawless record, but his latest case is unlike any other. A serial killer leaves no trace except a single black feather at each crime scene. As Haruto dives deeper into the case, he discovers the existence of a secret society pulling the strings behind the scenes. With his own life on the line, Haruto must unravel the web of lies before the killer strikes again.",
    # llama 3
    "In a world where humanity has colonized other planets, a group of friends discovers a mysterious phenomenon that allows them to communicate with their past and future selves. As they navigate the consequences of altering the timeline, they must confront an ancient evil that threatens to destroy the fabric of reality. With time running out, can they find a way to restore balance to the universe before it's too late?",
    "In a land ravaged by war, a young orphan discovers she is the chosen one destined to save the world from an ancient curse. Armed with a magical sword and accompanied by a motley group of companions, she embarks on a perilous quest to defeat the dark sorcerer who has brought about the devastation. Along the way, she must confront her own demons and face the ultimate test: saving the world from eternal darkness.",
    "After a tragic accident leaves her with a broken heart and a shattered sense of identity, high school student Kana returns to her hometown to pick up the pieces. As she navigates the treacherous waters of small-town gossip and old friendships, she must confront the secrets and lies that have haunted her family for generations. Can she find a way to heal and move forward, or will the wounds of the past forever define her?",
    "In a world where corporations have replaced governments, a group of elite mercenaries known as the \"Phoenix Brigade\" must take down corrupt CEOs who are hell-bent on destroying the planet. Led by the enigmatic and deadly leader, Kaito, they must fight their way through treacherous landscapes and rival gangs to stop the evil conglomerate that threatens to burn the world to ashes.",
    "Welcome to Camp Sunshine, a summer camp for misfit kids who are more likely to get into trouble than make friends. Led by the hapless counselor, Max, they embark on wacky adventures and outrageous pranks as they navigate the ups and downs of adolescence. But when a group of rival campers from the prestigious Camp Elite arrive on the scene, it's game on! Can our ragtag crew outdo their snobbish foes and have the most epic summer ever?",
    "In the sleepy town of Ravenswood, a mysterious phenomenon has awakened an ancient evil that threatens to consume everything in its path. As the townspeople are consumed by an otherworldly darkness, a small group of survivors must band together to uncover the secrets behind the curse and find a way to stop it before it's too late. But as they delve deeper into the mystery, they'll discover that some terrors are better left unspoken.",
    "In the quaint town of Petalville, a group of flower shop owners compete for the title of Best Florist in the annual Flower Festival. Amidst the competition and romance, our protagonist, Sakura, finds herself caught between her childhood sweetheart, Taro, and the charming newcomer, Ryo. As they navigate the ups and downs of love and rivalry, Sakura must confront her own feelings and make a choice that will change her life forever.",
    # gemma2
    "Maya, a young herbalist with the uncanny ability to speak to plants, discovers her village is threatened by an ancient curse. Guided by the whispers of the forest, she embarks on a perilous journey to find the legendary Sunstone, the only artifact capable of breaking the curse and restoring balance to the land.",
    "In a future where consciousness can be uploaded into virtual realities, Kai, a skilled hacker grieving the loss of his loved one, stumbles upon a hidden program: Echo. It promises to recreate lost memories but comes with a dangerous price.  Kai must navigate the treacherous world of digital ghosts and confront the ethics of artificial immortality.",
    "Hana, a shy college student who dreams of becoming an astronomer, takes a part-time job at a cozy cafe known for its breathtaking rooftop views. There she meets Ren, a charismatic musician with a hidden past. As they share late-night conversations under the stars, their shared passion for beauty and longing ignite a delicate romance.",
    "In a world ravaged by monstrous creatures known as Chimera, a band of skilled warriors known as the Crimson Blades stand as humanity's last hope. Leading them is Akira, a stoic swordsman haunted by a tragic past.  As they battle through treacherous landscapes and face insurmountable odds, Akira must confront his inner demons and unlock the true potential of his legendary blade.",
    "Aiko, a gifted librarian with a photographic memory, discovers a hidden message within a centuries-old book. It leads her down a rabbit hole of conspiracy, secret societies, and forgotten history.  With the help of a cynical detective and a reclusive historian, she must decipher the clues before the truth is silenced forever.",
    # mistral s
    "In the kingdom of Astraeus, where magic is outlawed, a young blacksmith named Elara discovers she possesses an ancient power. When her village is attacked by shadow creatures, she embarks on a journey to restore balance and uncover the truth behind her lineage. Along the way, she meets allies with unique abilities who help her challenge the tyrannical king and his dark forces.",
    "Set in a small town known for its cherry blossoms, high school student Hiroki falls in love with Yumi, a new transfer student who loves to paint. As they spend more time together, Hiroki learns about Yumi's past and the pain she carries. Through their growing bond, they find solace and healing under the soft glow of the cherry blossoms, facing their fears together.",
    "In a future where humans colonize space, a brilliant engineer named Lyra is tasked with investigating mysterious alien signals. As she unravels the truth, she realizes that these signals are not just messages from an unknown civilization but also hold the key to unlocking humanity's next evolutionary step. Alongside her team, Lyra ventures into the cosmos, facing both technological and existential challenges.",
    "In a quiet seaside town, a humble bakery named \"Daily Bread\" becomes a hub for the community's daily lives. Follow the baker, his apprentices, and their customers as they share stories of love, loss, and laughter over freshly baked pastries. This heartwarming series captures the essence of simple pleasures and the beauty in everyday interactions.",
    "In a world where swords possess mystical powers, legendary bladesmith Kaito loses his memory after a catastrophic battle. Accompanied by a feisty thief and an enigmatic sorcerer, he embarks on a quest to reclaim his past and restore the balance of power in a land threatened by dark forces. As they journey through treacherous terrains, Kaito's blades awaken, revealing secrets that challenge everything he knows about himself and the world.",
    "In a modern-day city, ancient yokai (supernatural creatures) coexist with humans but are bound by strict rules. When a series of mysterious disappearances occur, a young exorcist named Akira teams up with a mischievous kitsune to uncover the truth. As they delve deeper into the case, they discover an ancient prophecy that threatens both worlds and must join forces to prevent a catastrophic event.",
    "Private investigator Aoi solves cases using her unique ability to see glimpses into the past. When she receives a cryptic message from an unknown sender, it leads her to a series of bizarre murders where time itself seems to be warped. As she digs deeper, Aoi uncovers a hidden society that manipulates time for their own nefarious purposes and becomes entangled in a web of deceit and danger.",
    "Underdog basketball team \"The Harmonics\" struggles to gain recognition despite their unconventional playing style inspired by music. When a talented but troubled player named Rei joins, the team faces backlash from traditionalists who disapprove of their methods. Through determination and unity, they prove that passion and creativity can overcome any obstacle on and off the court."
]

assert len(origin) == len(new_reviews)

# Токенизация нескольких отзывов
inputs = tokenizer(new_reviews, return_tensors='pt', padding=True, truncation=True, max_length=512)

# Прогнозирование рейтингов
with torch.no_grad():
    outputs = model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])
    predicted_ratings = outputs.squeeze().tolist()  # Конвертируем предсказания в список

# Токенизация нескольких отзывов
inputs = tokenizer(new_reviews, return_tensors='pt', padding=True, truncation=True, max_length=512)

# Прогнозирование рейтингов
with torch.no_grad():
    outputs = model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])
    predicted_ratings = outputs.squeeze().tolist()  # Конвертируем предсказания в список

for review, rating, origin in sorted(zip(new_reviews, predicted_ratings, origin), key=lambda x: -x[1]):
    print(f'Review: {review}')
    print(f'Predicted Rating: {rating * 10:.2f} {origin}\n')
