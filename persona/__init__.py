"""Web Persona 人物角色创建与应用工具包

基于《赢在用户：Web人物角色创建和应用实践指南》全书知识体系构建。
覆盖 SKILL.md 全部 A-J 模块的执行能力。

快速开始::

    from persona import PersonaSkill
    skill = PersonaSkill("我的产品")

    # 生成访谈提纲
    guide = skill.generate_interview("用户访谈", ["goals", "behaviors", "pain_points"])

    # 设计调查问卷
    survey = skill.generate_survey("需求调研", "needs", pain_points=["找酒店耗时"])

    # 创建人物角色
    skill.add_persona("小明", "效率型用户", "primary", "我只想快速完成",
                      goals=["快速完成任务"], behaviors=["频繁使用"],
                      attitudes=["追求效率"], bio="小明是一位忙碌的白领...")
    print(skill.render_all_personas())
"""

__version__ = "3.3.26"
