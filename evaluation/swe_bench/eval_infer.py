    LLMConfig,
    default_llm = LLMConfig(
        draft_editor=LLMConfig()  # just to prevent eval errors
    )
    config.set_llm_config(default_llm)