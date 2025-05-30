import streamlit as st
import datetime

st.set_page_config(page_title="英语写作辅助平台（离线演示）", layout="wide")
st.title("✍ 英语写作辅助平台（离线演示）")

st.markdown("请输入你的英文段落，点击下方按钮，我们将为你模拟提供纠错、润色、评分和写作反思建议：")

user_input = st.text_area("输入英文段落", height=300)

if st.button("开始模拟分析"):
    if not user_input.strip():
        st.warning("请输入一些英文文本")
    else:
        with st.spinner("模拟分析中..."):
            # 模拟响应内容
            mock_correction = user_input.replace("i", "I").replace("dont", "don't") + " (grammar fixed)"

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("修正建议")
                st.write(mock_correction)

                st.subheader("评分")
                st.write("""
                - Logic: 7/10
                - Language Use: 6/10
                - Structure: 8/10
                """)

            with col2:
                st.subheader("写作策略建议（融合元认知引导）")
                st.markdown("""
                - **计划阶段**：在写作前，想一想你想表达的主要观点和结构框架。
                - **监控阶段**：在写作中不断问自己：这句话是否支持中心论点？语法正确吗？
                - **评估阶段**：完成后自查内容是否连贯，是否达成了写作目标。
                """)

                st.subheader("🪞 写作反思建议")
                st.markdown("""
                - 在未来写作中，可以更加注意句子衔接与段落过渡。
                - 尝试在修改时朗读文章，帮助发现不通顺的部分。
                """)

            st.markdown("---")
            st.download_button(
                label="📥 下载分析报告 (Word 文档)",
                data=f"""
英语写作分析报告 - {datetime.date.today()}

原始内容：
{user_input}

修正建议：
{mock_correction}

评分：
- Logic: 7/10
- Language Use: 6/10
- Structure: 8/10

写作策略建议：
1. 计划写作目标与结构
2. 监控语法与逻辑
3. 评估成果与反馈

写作反思：
- 强化结构连贯性
- 利用朗读发现问题
                """,
                file_name="writing_feedback.docx",
                mime="text/plain"
            )

st.markdown("---")
st.markdown("当前为离线模拟版本。如需真实 AI 分析，请配置 OpenAI API Key。")
