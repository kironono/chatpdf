from pathlib import Path

from llama_index import LLMPredictor, PromptHelper, ServiceContext
from langchain.chat_models import ChatOpenAI


class Config:

    def __init__(self, index_file=None):
        if index_file is None:
            index_file = self._default_index_file()
        self.index_file = index_file
        
        self.llm_predictor = LLMPredictor(
                llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))

        # set maximum input size
        max_input_size = 4096
        # set number of output tokens
        num_output = 256
        # set maximum chunk overlap
        max_chunk_overlap = 20

        self.prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)
        
        self.service_context = ServiceContext.from_defaults(
                llm_predictor=self.llm_predictor,
                prompt_helper=self.prompt_helper)

    def _default_index_file(self):
        config_dir = self._config_dir()
        return config_dir.joinpath("index.json")

    def _config_dir(self):
        return Path.home().joinpath(".config", "chatpdf")
