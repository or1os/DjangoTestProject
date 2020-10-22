from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["username"] = "まさき"
        return context


class About(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["num_services"] = "12345678"
        context["skills"] = [
            "python",
            "C++",
            "javascript",
            "Rust",
            "Go",
        ]
        return context
