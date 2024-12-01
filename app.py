import streamlit as st
from transformers import pipeline
import random

 # Title of the app
st.title("MoodCheck: Analyze, Improve, Thrive")

# Instructions
st.write("**Welcome! We will help you detect your mood and suggest recommendations to improve it.**")
st.write("**Please enter a short sentence or paragraph to analyze your mood.**")
st.write()

# Input text from the user
user_input = st.text_area("Your mood input:")

# Load the pre-trained emotion detection model
@st.cache_resource
def load_model():
    return pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

model = load_model()

def contextual_analysis(text):
    # Define sentiment words (positive and negative)
    sentiment_words = {
        "negative": ['angry', 'mad', 'irritated', 'frustrated', 'sad', 'upset', 'depressed', 'scared', 'nervous'],
        "positive": ['happy', 'joyful', 'excited', 'hopeful', 'content']
    }

    # Lists of words indicating specific emotions
    emotion_indicators = {
        "anger": ['angry', 'mad', 'irritated', 'frustrated', 'rage', 'furious'],
        "joy": ['happy', 'excited', 'joyful', 'thrilled', 'amazing', 'content', 'fun'],
        "sadness": ['sad', 'upset', 'depressed', 'down', 'grief', 'lonely'],
        "fear": ['fear', 'scared', 'terrified', 'nervous', 'afraid', 'anxious'],
        "surprise": ['surprised', 'shocked', 'unexpected', 'amazed', 'astonished'],
        "disgust": ['disgust', 'gross', 'sick', 'nauseous', 'repulsed'],
        "stress": ['work', 'pending', 'stress', 'pressure', 'deadline', 'overwhelmed', 'busy'],
        "tired": ["tired", "exhausted", "fatigue", "drained", "worn out", "low energy", "sleepy", "weary", "drowsy", "burnt out"],
        "neutral": ['normal', 'fine', 'okay', 'alright'],
        "grumpy": ['grumpy', 'moody', 'irritable', 'snappy'],
        "sick": ['sick', 'unwell', 'ill', 'queasy', 'dizzy', 'feverish'],
        "confused": ['confused', 'perplexed', 'lost', 'uncertain', 'puzzled'],
        "excited": ['excited', 'eager', 'enthusiastic', 'elated', 'ecstatic', 'anticipating'],
        "love": ['love', 'affection', 'caring', 'fond', 'adoring', 'devoted', 'cherish'],
        "loneliness": ['lonely', 'isolated', 'alone', 'abandoned', 'forsaken'],
        "hope": ['hope', 'optimistic', 'believe', 'trust', 'faith'],
        "shame": ['shame', 'guilt', 'embarrassed', 'humiliated', 'regret'],
        "pride": ['proud', 'accomplished', 'successful', 'dignity', 'triumphant'],
        "relief": ['relieved', 'comforted', 'soothed', 'unburdened', 'eased'],
        "boredom": ['bored', 'uninterested', 'dull', 'tedious', 'listless'],
        "jealousy": ['jealous', 'envy', 'resentful', 'covet', 'grudge'],
        "embarrassment": ['embarrassed', 'awkward', 'blushed', 'uncomfortable'],
        "curiosity": ['curious', 'inquisitive', 'interested', 'wondering', 'exploring'],
        "determination": ['determined', 'focused', 'resilient', 'persistent', 'motivated'],
        "contentment": ['content', 'peaceful', 'calm', 'satisfied', 'fulfilled']
    }

    detected_emotions = []
    for emotion, keywords in emotion_indicators.items():
        if any(word in text.lower() for word in keywords):
            detected_emotions.append(emotion)
    
    return detected_emotions

# Function to return tips based on emotion
def stress_relief_tips(emotion):
    tips = {
        "anger": [
            "💥 **Quick Exercise**: Try a 1-minute burst of jumping jacks or running on the spot. Physical activity helps to release tension.",
            "🌬 **Mindful Breathing**: Close your eyes, take 5 slow, deep breaths. Inhale for 4 seconds, hold for 4, and exhale for 6.",
            "📝 **Anger Journal**: Write down what made you angry. Sometimes, getting it all out on paper helps you see things clearly.",
            "🛀 **Take a Warm Bath**: A warm bath can help calm your body and mind, easing physical tension.",
            "📞 **Talk to Someone**: Share your feelings with a friend or family member who can offer a supportive ear."
        ],
        "stress": [
            "🌊 **Visualization Exercise**: Close your eyes and imagine lying on a calm beach. Let the sound of the waves soothe your mind.",
            "☕ **Take a Break**: Stepping away from your desk for just 5 minutes with a warm beverage can reset your mind.",
            "💃 **Dance It Out**: Play your favorite song and move your body for a minute. Dance helps release those stress hormones!",
            "🧘 **Stretching**: Try a quick stretching routine to relieve tension from your body.",
            "📚 **Read a Book**: Take a short break by diving into a few pages of your favorite book to give your mind a break."
        ],
        "sadness": [
            "🌟 **Acts of Kindness**: Send a message or compliment to a friend. Helping others can boost your own mood.",
            "🎨 **Expressive Art**: Pick up a pen or brush and just let your emotions flow. Creating without judgment can relieve sadness.",
            "🙏 **Gratitude Practice**: Write down 3 things you’re thankful for today. Gratitude is a powerful tool for improving your mood.",
            "🌸 **Take a Nature Walk**: Go outside and enjoy the fresh air and nature. A short walk can help shift your perspective.",
            "🧸 **Cuddle Up**: Sometimes hugging a stuffed animal or wrapping yourself in a blanket helps bring comfort and warmth."
        ],
        "fear": [
            "💪 **Power Pose**: Stand like a superhero with your hands on your hips and chest open. Hold for 2 minutes. It boosts confidence and reduces anxiety.",
            "🌍 **Grounding Exercise**: 5 things you can see, 4 you can feel, 3 you can hear, 2 you can smell, and 1 you can taste. This brings you back to the present moment.",
            "🤔 **Challenge Your Fear**: Ask yourself, ‘What’s the worst that can happen?’ When you challenge your fear, it often seems less scary.",
            "🧘 **Deep Breathing**: Close your eyes and take 5 slow breaths in through your nose and out through your mouth. It helps calm your nerves.",
            "📖 **Positive Affirmations**: Repeat a positive affirmation like 'I am strong, and I can handle this.' Reminding yourself of your inner strength can ease fear."
        ],
        "grumpy": [
            "🧃 **Hydrate**: Sometimes feeling grumpy can stem from dehydration. Drink a glass of water or juice to refresh yourself.",
            "🌿 **Fresh Air**: Step outside for a few minutes. A change of scenery can work wonders for a bad mood.",
            "🎵 **Happy Playlist**: Play an upbeat song you love. Music has a magical way of improving moods.",
            "🍫 **Small Treat**: Indulge in a small snack you love—chocolate or fruit. It’s a quick pick-me-up.",
            "😄 **Smile Trick**: Try smiling even if you don’t feel like it. Sometimes, the action itself can influence your mood."
        ],
        "embarrassed": [
            "🤗 **Talk to a Friend**: Share your experience with someone you trust. Laughing it off together can help ease the feeling.",
            "🧘 **Deep Breathing**: Close your eyes and take slow, deep breaths. This helps calm the immediate sense of embarrassment.",
            "📚 **Perspective Shift**: Remember, everyone makes mistakes or has awkward moments. It’s part of being human.",
            "💪 **Own It**: Sometimes acknowledging it with a smile or joke can disarm the situation and make it less awkward.",
            "🌈 **Focus Forward**: Shift your attention to something else—like a fun plan or hobby—to move on quickly."
        ],
        "sick": [
            "🛌 **Rest**: Allow yourself time to rest. Pushing through sickness only prolongs recovery.",
            "☕ **Warm Comfort**: Drink warm tea with honey or soup to soothe your body.",
            "🌡️ **Care Routine**: Use a cozy blanket, heating pad, or humidifier for extra comfort.",
            "📺 **Light Entertainment**: Watch a light, feel-good show or movie to distract yourself.",
            "🧴 **Aromatherapy**: Use calming essential oils like lavender or eucalyptus to ease discomfort."
        ],
        "loneliness": [
            "📞 **Reach Out**: Call or message a friend or family member. Even a small conversation can lift your mood.",
            "🐾 **Pet Love**: If you have a pet, spend time playing or cuddling with them. They’re great companions.",
            "📝 **Journaling**: Write down your feelings. It can help you process emotions and feel less alone.",
            "🤝 **Online Groups**: Join an online community or hobby group to connect with like-minded people.",
            "🌄 **Explore**: Go for a walk in a park or visit a public place. Being around others (even strangers) can help ease loneliness."
        ],
        "shame": [
            "🛑 **Forgive Yourself**: Remember, everyone makes mistakes. Be kind to yourself as you would to a friend.",
            "📚 **Learn from It**: Focus on what you can learn from the situation instead of dwelling on the past.",
            "❤️ **Compassion Practice**: Repeat a kind affirmation like, 'I am human, and it’s okay to make mistakes.'",
            "🗨️ **Talk It Out**: Sharing with someone trustworthy can help you gain a new perspective.",
            "🌸 **Let It Go**: Engage in an activity you enjoy to distract yourself and move forward."
        ],
        "jealousy": [
            "✍️ **Gratitude List**: Write down 3 things you’re thankful for to shift focus to the positives in your life.",
            "🌟 **Turn It Around**: Use the feeling as motivation to work toward your own goals instead of comparing yourself to others.",
            "🛑 **Limit Social Media**: Take a break from scrolling online, as it often fuels unnecessary comparisons.",
            "🎨 **Channel It**: Dive into a creative outlet like drawing, writing, or a hobby to redirect your energy.",
            "🧘 **Mindfulness**: Focus on the present moment and what brings you joy right now."
        ],
        "boredom": [
            "🎲 **Try Something New**: Learn a new skill, try a different recipe, or explore a hobby you’ve never done before.",
            "🎮 **Fun Games**: Play a quick online game or do a crossword puzzle to challenge your mind.",
            "🧹 **Declutter**: Organize a drawer or your desk. It’s productive and gives a sense of accomplishment.",
            "📖 **Dive into a Book**: Start reading a novel or article you’ve been meaning to check out.",
            "🎶 **Podcasts & Music**: Listen to an interesting podcast or a new playlist to keep your mind engaged."
        ],
       "tired": [
            "💤 **Power Nap**: Take a 10-15 minute nap to refresh your mind and recharge your energy.",
            "🧘 **Stretching**: Do some light stretches to get your blood flowing and ease tension.",
            "☕ **Hydrate and Refresh**: Drink a glass of water to rehydrate your body, or try a caffeine-free herbal tea.",
            "🌞 **Natural Light**: Step outside and get some fresh air and sunlight to boost your mood and energy.",
            "🎶 **Listen to Energizing Music**: Play some upbeat music to lift your spirits and help you feel more awake."
       ]

    }

    # Return the tips for the detected emotion
    return tips.get(emotion, ["You're doing great! Remember to take care of yourself."])


# Function to analyze emotion based on the text input
def analyze_emotion(text):
    # First, check for contextual indications (stress, joy, etc.)
    detected_emotions = contextual_analysis(text)
    
    if detected_emotions:
        # Return first matching emotion with a high confidence (assuming contextual rules give good results)
        return ", ".join(detected_emotions), 1.00

    # If no strong context detected, analyze using the model
    sentences = text.split(".")  # Split text into sentences
    emotions = []
    confidence_scores = []
    
    # Analyze each sentence and collect emotions and confidence scores
    for sentence in sentences:
        if sentence.strip():  # Skip empty sentences
            result = model(sentence.strip())
            emotions.append(result[0]['label'])
            confidence_scores.append(result[0]['score'])  # Collect confidence scores
    
    # Detect mixed emotions: If different emotions appear in the same text
    unique_emotions = set(emotions)  # Get unique emotions from sentences
    if len(unique_emotions) > 1:
        return "Mixed Emotions: " + ", ".join(unique_emotions), max(confidence_scores)
    
    # Handle specific emotions
    return unique_emotions.pop(), max(confidence_scores)

# Analyze and display mood
if user_input:
    st.write("You wrote: ", user_input)
    # Analyze mood using the model
    final_emotion, confidence = analyze_emotion(user_input)
    # Convert confidence to percentage
    confidence_percentage = confidence * 100
    # Display results
    st.write(f"**Detected Mood:** {final_emotion}")
    st.write(f"**Confidence Level:** {confidence_percentage:.2f}%")

    # Handle mixed emotions
    emotions_to_show = final_emotion.replace("Mixed Emotions: ", "").split(", ")

    # Check if we need to reset the tip list
    if 'tips_list' not in st.session_state or st.session_state.tip_index >= len(st.session_state.tips_list):
        # Initialize or reset the tip list and index when a new emotion is detected
        st.session_state.tips_list = []

        # Generate tips for all detected emotions
        for emotion in emotions_to_show:
            emotion_tips = stress_relief_tips(emotion)
            if emotion_tips[0] != "You're doing great! Remember to take care of yourself.":
                st.session_state.tips_list.extend(emotion_tips)

        # Reset index when new input is detected
        st.session_state.tip_index = 0

    # Show the current tip
    if st.session_state.tips_list:
        current_tip = st.session_state.tips_list[st.session_state.tip_index]
        st.write(current_tip)

        # Next Tip button functionality
        if st.button("Next Tip"):
            st.session_state.tip_index = (st.session_state.tip_index + 1) % len(st.session_state.tips_list)
    else:
        st.write("You're doing great! Remember to take care of yourself.")
else:
    st.write("Please enter some text to analyze your mood.")
