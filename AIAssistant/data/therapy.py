# Generate sample therapy notes for the last 3 Saturdays
therapy_notes = """
**Date:** Saturday, December 23, 2023

### Personal Therapy Notes
Today’s session was a bit heavy. I told Dr. Emily about how the holiday season has been triggering for me. There’s so much pressure to be cheerful and social, and I feel like I’m failing at it. I admitted to her that I’ve been avoiding family gatherings because I’m worried about being judged or asked questions I don’t know how to answer.

She reminded me that it’s okay to set boundaries and protect my mental health, even if it means saying no to certain events. We also talked about how I could prepare simple responses to common questions, so I don’t feel so caught off guard.

I shared how I’ve been keeping up with the gratitude journal from last week. It’s been harder on bad days, but it’s helping me notice the small good things, like enjoying a walk or finishing a task.

Before we ended, Dr. Emily asked me to try practicing mindfulness during family interactions this week—staying present and observing my thoughts without judgment. It feels like a big ask, but I’ll try.

---

**Date:** Saturday, December 16, 2023

### Personal Therapy Notes
Today, I went to see Dr. Emily for my weekly therapy session. I’ve been feeling slightly better compared to the last few weeks, but mornings are still tough. I told her how I’ve been struggling to get out of bed and how overwhelming everything feels when the day starts.

We talked about some of the anxiety triggers I’ve been dealing with. I shared how crowded spaces make me feel panicky and how group presentations are still a nightmare for me. Dr. Emily helped me unpack why these situations feel so intense, and I realized it’s because I keep telling myself things like, “I’m going to mess up,” or “Everyone’s judging me.”

Dr. Emily reminded me about the thought reframing exercises we’ve been practicing. She said I should try replacing those negative thoughts with something more balanced, like, “I’ve prepared for this, and it’s okay to make small mistakes.” Honestly, it still feels awkward doing this, but I admitted that it worked in smaller moments last week.

She also asked me to reflect on any positives from this week. It took me a second, but I mentioned how I completed an assignment on time and even texted a friend to catch up. That felt good. Dr. Emily called these “small wins” and said I need to acknowledge them more because they’re important steps forward.

We also went over some breathing techniques again—she calls it box-breathing. It’s where you inhale for 4 seconds, hold your breath for 4 seconds, and exhale for 4 seconds. I tried it in the session, and it actually helped me feel a little calmer. I’m going to practice this more during the week, especially when my anxiety spikes.

Before we wrapped up, Dr. Emily suggested that I start writing three things I like about myself or things I’ve done well each day. She says it’ll help me build self-compassion, which I’ve been seriously lacking. I don’t know if I’ll stick to it, but I’ll give it a shot.

---

**Date:** Saturday, December 9, 2023

### Personal Therapy Notes
This week has been rough. I told Dr. Emily how I’ve been feeling more down than usual and having trouble concentrating on anything. Even small tasks like doing the dishes feel like climbing a mountain.

Dr. Emily asked me about my sleep, and I admitted that I’ve been staying up late scrolling on my phone. She suggested trying to set a consistent bedtime and turning off screens at least 30 minutes before bed. I’m not sure if it’ll help, but it’s worth a try.

We also talked about my fear of being a burden to others. I shared how I avoid reaching out to friends because I’m worried they’ll think I’m too much to handle. Dr. Emily challenged me to think about how I feel when my friends reach out to me—it’s never a burden, and she said it’s likely they feel the same way about me.

She encouraged me to take one small step this week, like texting one close friend just to say hi. That feels scary, but also doable.

At the end of the session, we talked about progress not being linear. She reminded me that it’s okay to have bad weeks and that they don’t erase the steps I’ve taken forward. I’m holding onto that thought as I head into this week.

---
"""

# Save the notes to a text file
file_path = "./therapy_notes_last_3_saturdays.txt"

with open(file_path, "w") as file:
    file.write(therapy_notes)

file_path
