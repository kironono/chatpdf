from llama_index import GPTSimpleVectorIndex


class Repl:

    def __init__(self, config):
        self.config = config

    def _load_index(self):
        self.index = GPTSimpleVectorIndex.load_from_disk(
                self.config.index_file,
                service_context=self.config.service_context)

    def _exec_query(self, query):
        response = self.index.query(query)
        return response.response

    def run(self):
        self._load_index()

        line = 0
        while True:
            line += 1
            user_input = input(f"[Question: {line}]> ")

            if user_input == "exit()":
                quit()
            elif user_input == "exit":
                print("Use `exit()` to exit.")
                continue

            try:
                anser = self._exec_query(user_input)
                print("Answer: ", end="")
                print(anser)
                print("")
            except Exception as error:
                if hasattr(error, "message"):
                    print(error.message)
                else:
                    print(error)
                pass
