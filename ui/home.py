# ui/home.py

import streamlit as st

from data.constants import MODE_CASE, MODE_DIRECT


def render_home():
    st.markdown(
        '<div class="main-title">교육용 근전도 판독 보조 앱</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="subtle">'
        '물리치료학과 학생과 임상물리치료사가 근전도검사와 신경전도검사의 결과를 '
        '임상 증상, 이학적 검사, 병변 위치 추론과 연결해 학습할 수 있도록 구성한 교육용 앱입니다.'
        '</div>',
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------
    # 학습 안내
    # ------------------------------------------------------------------
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="big-section-title">📖 학습 안내</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="case-bullet">
            <span class="label-strong text-blue">• 사례 학습 모드:</span>
            실제 수치 결과표를 자세히 읽기 전에, 환자의 증상·이학적 검사·간략화된 근전도 소견을 바탕으로
            “어느 척수 수준 또는 어느 말초신경 가지가 손상되었는가?”를 단계적으로 추론하는 모드입니다.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="case-bullet">
            <span class="label-strong text-blue">• 가상 결과표 판독학습:</span>
            실제 임상 근전도 결과표와 유사한 형식으로 감각신경전도검사, 운동신경전도검사, 침근전도검사 수치를 제시하고,
            각 표를 어떻게 읽고 요약해야 하는지 훈련하는 모드입니다.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 요청 1 반영: 고급 교육포인트를 요약 나열이 아닌 문장형으로 수정
    st.markdown(
        """
        <div class="case-bullet">
            <span class="label-strong text-blue">• 고급 교육 포인트:</span>
            이 앱의 핵심은 단순히 “정상/비정상”을 외우는 것이 아니라,
            감각신경활동전위(SNAP), 복합근육활동전위(CMAP), 침근전도 자발전위와 운동단위동원 양상을
            서로 연결하여 신경뿌리병증, 신경얼기병증, 단일 말초신경병증, 다발신경병증, 반사경로 이상을
            실제 임상 추론 과정처럼 구분하는 데 있습니다.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # 교육용 경고
    # ------------------------------------------------------------------
    st.markdown(
        """
        <div class="warn-card">
            <div class="case-bullet-strong text-red">
                ⚠️ 본 앱은 근전도 판독 교육을 위한 시뮬레이터이며, 실제 의학적 진단·처방·치료 결정을 대체하지 않습니다.
            </div>
            <div class="case-bullet">
                실제 환자에게 적용할 때는 의사, 임상전문가, 영상검사, 병력, 신체검사 결과와 함께 종합해야 합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------
    # 모드 선택
    # ------------------------------------------------------------------
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📋 진행할 학습 모드 선택</div>', unsafe_allow_html=True)

    display_modes = {
        MODE_CASE: "사례 학습 모드",
        MODE_DIRECT: "가상 결과표 판독학습",
    }

    selected_display = st.radio(
        "모드 선택",
        options=list(display_modes.values()),
        label_visibility="collapsed",
        key="home_mode_selector",
    )

    mode = [k for k, v in display_modes.items() if v == selected_display][0]

    if mode == MODE_CASE:
        st.markdown(
            """
            <div class="info-card" style="margin-top: 12px;">
                <div class="case-bullet-strong text-blue">사례 학습 모드의 목적</div>
                <div class="case-bullet">
                    이 모드는 <b>임상 추론 훈련</b>에 초점을 둡니다.
                    검사 결과는 “진폭 감소”, “잠복기 지연”, “감각전도 보존”, “비정상 자발전위 출현”처럼
                    학생이 이해하기 쉬운 형태로 간략화됩니다.
                </div>
                <div class="case-bullet">
                    학습자는 환자의 주증상, 감각분포, 근력저하, 반사 변화, 간략 근전도 소견을 종합하여
                    구체적인 의심 질환과 병변 위치를 추론합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="info-card" style="margin-top: 12px;">
                <div class="case-bullet-strong text-blue">가상 결과표 판독학습의 목적</div>
                <div class="case-bullet">
                    이 모드는 <b>실제 결과표 판독 훈련</b>에 초점을 둡니다.
                    감각신경전도검사와 운동신경전도검사의 자극 위치별 진폭·잠복기 수치,
                    침근전도의 휴식 시 반응과 수의수축 시 운동단위동원 양상을 표로 제시합니다.
                </div>
                <div class="case-bullet">
                    학습자는 표를 읽고, 정상측 대비 변화와 병변 위치를 해석한 뒤
                    의심 질환, 손상 위치, 감별진단, 추가 검사를 실제 임상 판독 흐름에 맞춰 정리합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="warn-card">
            <div class="finding-highlight" style="color:#b45309;">🎓 근전도 판독 기준 팁</div>
            <div class="case-bullet">
                • <b>진폭 감소</b>: 병변측 진폭이 정상측 대비 약 50% 이하로 감소하면 축삭 손상 가능성을 의심합니다.
            </div>
            <div class="case-bullet">
                • <b>잠복기 지연</b>: 병변측 잠복기가 정상측 대비 약 130% 이상 길어지면 말이집탈락 또는 국소 전도 지연 가능성을 의심합니다.
            </div>
            <div class="case-bullet">
                • <b>감각전도 보존</b>: 신경뿌리병증은 뒤뿌리신경절보다 몸쪽 병변이므로 말초 감각신경활동전위가 보존되는 경우가 많습니다.
            </div>
            <div class="case-bullet">
                • <b>침근전도 이상</b>: 휴식 시 비정상 자발전위와 수의수축 시 운동단위동원 감소를 함께 보면 운동축삭 손상과 병변 분절을 추정할 수 있습니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="start-button-wrap">', unsafe_allow_html=True)

    if st.button("🚀 학습 시작", type="primary", use_container_width=True):
        st.session_state["mode"] = mode
        if mode == MODE_CASE:
            st.session_state["screen"] = "case_list"
        else:
            st.session_state["screen"] = "input_learning"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
