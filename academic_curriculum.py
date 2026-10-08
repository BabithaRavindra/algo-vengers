# academic_curriculum.py - Master Academic Curriculum Aggregator
from academic_data_part1 import PART1_TOPICS
from academic_data_part2 import PART2_TOPICS
from academic_data_part3 import PART3_TOPICS
from academic_data_part4 import PART4_TOPICS

ALL_TOPICS = []
ALL_TOPICS.extend(PART1_TOPICS)
ALL_TOPICS.extend(PART2_TOPICS)
ALL_TOPICS.extend(PART3_TOPICS)
ALL_TOPICS.extend(PART4_TOPICS)

print(f"Total topics loaded in academic_curriculum: {len(ALL_TOPICS)}")

if __name__ == "__main__":
    for i, t in enumerate(ALL_TOPICS):
        print(f"[{i+1:02d}] {t['filename']:35} | {t['hero_name']:18} | Quiz: {len(t['quiz'])} questions")
