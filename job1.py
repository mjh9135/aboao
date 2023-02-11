import streamlit as st
import openai

# Use OpenAI API key to authenticate
import os

openai_api_key = os.environ.get("OPENAI_API_KEY")

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def main():
    st.title("AI 职业推荐和个人介绍生成器")

    interests = st.text_area("请输入你的个人喜好特点:")
    personality = st.text_area("请输入你的性格特征:")
    experience = st.text_area("请输入你的工作经历:")
    skills = st.text_area("请输入你的所学技能课程:")
    desired_career = st.text_area("请输入你的期望职业岗位:")

    # 使用 OpenAI API 推荐职业岗位
    # if st.button("推荐职业岗位"):
    #     model_engine = "text-davinci-003"
    #     prompt = f"根据输入的个人信息，推荐适合的职业岗位，并写一份工作的自我介绍。个人喜好特点: {interests}, 性格特征: {personality}, 工作经历: {experience}, 所学技能课程: {skills}, 期望职业岗位: {desired_career}"
    #
    #     completions = openai.Completion.create(
    #         engine=model_engine,
    #         prompt=prompt,
    #         max_tokens=1024,
    #         n=1,
    #         stop=None,
    #         temperature=0.5,
    #     )
    #
    #     message = completions.choices[0].text
    #     st.write("推荐的职业岗位: ", message)

    if st.button("生成"):
        # prompt = (f"我的个人喜好特点: {interests}. "
        #           f"我的性格特征: {personality}. "
        #           f"我做过的工作: {experience}. "
        #           f"我学到了一些技能: {skills}. "
        #           f"我想当一名:{desired_career}. "
        #           f"你能为我推荐一个适合我的职业，并写一份工作的自我介绍吗?")
        prompt = f"根据输入的个人信息，推荐适合的职业岗位，并写一份工作的自我推荐介绍。个人喜好特点: {interests}, 性格特征: {personality}, 工作经历: {experience}, 所学技能课程: {skills}, 期望职业岗位: {desired_career}"
        career_recommendation = generate_text(prompt)
        st.success(career_recommendation)

    st.write("This tool is powered by OpenAI.")

if __name__ == "__main__":
    main()
