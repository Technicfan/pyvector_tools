import customtkinter as ctk
import webbrowser as wb
import vector_tools

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # color scheme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # root window
        self.geometry("550x575")
        self.title("vector tools")
        self.resizable(False, False)
        self.btnDimensions = ctk.CTkSegmentedButton(self, values=["2", "3"], command=self.btnDimensions_callback)
        self.btnDimensions.set("3")
        self.btnDimensions.place(relx=0.22, rely=0.02, anchor=ctk.NW)
        self.lbl1 = ctk.CTkLabel(self, text="Dimensionen: ")
        self.lbl1.place(relx=0.05, rely=0.02, anchor=ctk.NW)
        self.lbl2 = ctk.CTkLabel(self, text="MIT License - Copyright (c) 2024 Technicfan")
        self.lbl2.place(relx=0.95, rely=0.02, anchor=ctk.NE)
        self.btnClose = ctk.CTkButton(self, text="Beenden", command=self.quit, width=75)
        self.btnClose.place(relx=0.98, rely=0.98, anchor=ctk.SE)
        self.btnGithub = ctk.CTkButton(self, text="https://github.com/Technicfan/pyvector_tools", 
                                        command=self.btnGithub_callback, fg_color="transparent", hover=False,
                                        text_color="#2fa572")
        self.btnGithub.place(relx=0.005, rely=0.995, anchor=ctk.SW)

        # tabview
        self.tab_view = ctk.CTkTabview(master=self, width=500, height=480)
        self.tab_view.place(relx=0.5, rely=0.49, anchor=ctk.CENTER)

        tv = self.tab_view
        tv.add("Vektor")
        tv.add("Vektorbeziehungen")
        tv.add("Gerade")
        tv.add("Geradenbeziehungen")

        # Vektor
        tv.btnVektor = ctk.CTkButton(tv.tab("Vektor"), text="Berechnen", command=self.btnVektor_callback)
        tv.btnVektor.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

        tv.edtVektorx = ctk.CTkEntry(tv.tab("Vektor"), placeholder_text="x")
        tv.edtVektorx.place(relx=0.5, rely=0.05, anchor=ctk.CENTER)

        tv.edtVektory = ctk.CTkEntry(tv.tab("Vektor"), placeholder_text="y")
        tv.edtVektory.place(relx=0.5, rely=0.12, anchor=ctk.CENTER)

        tv.edtVektorz = ctk.CTkEntry(tv.tab("Vektor"), placeholder_text="z")
        tv.edtVektorz.place(relx=0.5, rely=0.19, anchor=ctk.CENTER)

        tv.lblVektor = ctk.CTkLabel(tv.tab("Vektor"), text="")
        tv.lblVektor.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        tv.lblVektorLength = ctk.CTkLabel(tv.tab("Vektor"), text="")
        tv.lblVektorLength.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        tv.lblVektorNormal = ctk.CTkLabel(tv.tab("Vektor"), text="")
        tv.lblVektorNormal.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

        # Vektorbeziehungen
        tv.btnVektoren = ctk.CTkButton(tv.tab("Vektorbeziehungen"), text="Berechnen", command=self.btnVektoren_callback)
        tv.btnVektoren.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

        tv.edtVektorenax = ctk.CTkEntry(tv.tab("Vektorbeziehungen"), placeholder_text="x")
        tv.edtVektorenax.place(relx=0.3, rely=0.05, anchor=ctk.CENTER)

        tv.edtVektorenay = ctk.CTkEntry(tv.tab("Vektorbeziehungen"), placeholder_text="y")
        tv.edtVektorenay.place(relx=0.3, rely=0.12, anchor=ctk.CENTER)

        tv.edtVektorenaz = ctk.CTkEntry(tv.tab("Vektorbeziehungen"), placeholder_text="z")
        tv.edtVektorenaz.place(relx=0.3, rely=0.19, anchor=ctk.CENTER)

        tv.edtVektorenbx = ctk.CTkEntry(tv.tab("Vektorbeziehungen"), placeholder_text="x")
        tv.edtVektorenbx.place(relx=0.7, rely=0.05, anchor=ctk.CENTER)

        tv.edtVektorenby = ctk.CTkEntry(tv.tab("Vektorbeziehungen"), placeholder_text="y")
        tv.edtVektorenby.place(relx=0.7, rely=0.12, anchor=ctk.CENTER)

        tv.edtVektorenbz = ctk.CTkEntry(tv.tab("Vektorbeziehungen"), placeholder_text="z")
        tv.edtVektorenbz.place(relx=0.7, rely=0.19, anchor=ctk.CENTER)

        tv.lblVektoren = ctk.CTkLabel(tv.tab("Vektorbeziehungen"), text="")
        tv.lblVektoren.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        tv.lblVektorenSkalar = ctk.CTkLabel(tv.tab("Vektorbeziehungen"), text="")
        tv.lblVektorenSkalar.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        tv.lblVektorenWinkel = ctk.CTkLabel(tv.tab("Vektorbeziehungen"), text="")
        tv.lblVektorenWinkel.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

        tv.lblVektorenNormal = ctk.CTkLabel(tv.tab("Vektorbeziehungen"), text="")
        tv.lblVektorenNormal.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

        # Gerade
        tv.btnGerade = ctk.CTkButton(tv.tab("Gerade"), text="Berechnen", command=self.btnGerade_callback)
        tv.btnGerade.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

        tv.lblGerade1 = ctk.CTkLabel(tv.tab("Gerade"), text="+ r * ")
        tv.lblGerade1.place(relx=0.5, rely=0.12, anchor=ctk.CENTER)

        tv.edtGeradesx = ctk.CTkEntry(tv.tab("Gerade"), placeholder_text="x")
        tv.edtGeradesx.place(relx=0.3, rely=0.05, anchor=ctk.CENTER)

        tv.edtGeradesy = ctk.CTkEntry(tv.tab("Gerade"), placeholder_text="y")
        tv.edtGeradesy.place(relx=0.3, rely=0.12, anchor=ctk.CENTER)

        tv.edtGeradesz = ctk.CTkEntry(tv.tab("Gerade"), placeholder_text="z")
        tv.edtGeradesz.place(relx=0.3, rely=0.19, anchor=ctk.CENTER)

        tv.edtGeraderx = ctk.CTkEntry(tv.tab("Gerade"), placeholder_text="x")
        tv.edtGeraderx.place(relx=0.7, rely=0.05, anchor=ctk.CENTER)

        tv.edtGeradery = ctk.CTkEntry(tv.tab("Gerade"), placeholder_text="y")
        tv.edtGeradery.place(relx=0.7, rely=0.12, anchor=ctk.CENTER)

        tv.edtGeraderz = ctk.CTkEntry(tv.tab("Gerade"), placeholder_text="z")
        tv.edtGeraderz.place(relx=0.7, rely=0.19, anchor=ctk.CENTER)

        tv.lblGerade = ctk.CTkLabel(tv.tab("Gerade"), text="")
        tv.lblGerade.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        tv.lblGeradeNormal = ctk.CTkLabel(tv.tab("Gerade"), text="")
        tv.lblGeradeNormal.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        tv.lblGeradeSpurpunkte = ctk.CTkLabel(tv.tab("Gerade"), text="")
        tv.lblGeradeSpurpunkte.place(relx=0.5, rely=0.675, anchor=ctk.N)

        # Geradenbeziehungen
        tv.btnGeraden = ctk.CTkButton(tv.tab("Geradenbeziehungen"), text="Berechnen", command=self.btnGeraden_callback)
        tv.btnGeraden.place(relx=0.5, rely=0.52, anchor=ctk.CENTER)

        tv.lblGeraden1 = ctk.CTkLabel(tv.tab("Geradenbeziehungen"), text="+ r * ")
        tv.lblGeraden1.place(relx=0.5, rely=0.12, anchor=ctk.CENTER)

        tv.edtGeradenasx = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="x")
        tv.edtGeradenasx.place(relx=0.3, rely=0.05, anchor=ctk.CENTER)

        tv.edtGeradenasy = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="y")
        tv.edtGeradenasy.place(relx=0.3, rely=0.12, anchor=ctk.CENTER)

        tv.edtGeradenasz = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="z")
        tv.edtGeradenasz.place(relx=0.3, rely=0.19, anchor=ctk.CENTER)

        tv.edtGeradenarx = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="x")
        tv.edtGeradenarx.place(relx=0.7, rely=0.05, anchor=ctk.CENTER)

        tv.edtGeradenary = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="y")
        tv.edtGeradenary.place(relx=0.7, rely=0.12, anchor=ctk.CENTER)

        tv.edtGeradenarz = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="z")
        tv.edtGeradenarz.place(relx=0.7, rely=0.19, anchor=ctk.CENTER)

        tv.lblGeraden2 = ctk.CTkLabel(tv.tab("Geradenbeziehungen"), text="+ s * ")
        tv.lblGeraden2.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

        tv.edtGeradenbsx = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="x")
        tv.edtGeradenbsx.place(relx=0.3, rely=0.28, anchor=ctk.CENTER)

        tv.edtGeradenbsy = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="y")
        tv.edtGeradenbsy.place(relx=0.3, rely=0.35, anchor=ctk.CENTER)

        tv.edtGeradenbsz = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="z")
        tv.edtGeradenbsz.place(relx=0.3, rely=0.42, anchor=ctk.CENTER)

        tv.edtGeradenbrx = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="x")
        tv.edtGeradenbrx.place(relx=0.7, rely=0.28, anchor=ctk.CENTER)

        tv.edtGeradenbry = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="y")
        tv.edtGeradenbry.place(relx=0.7, rely=0.35, anchor=ctk.CENTER)

        tv.edtGeradenbrz = ctk.CTkEntry(tv.tab("Geradenbeziehungen"), placeholder_text="z")
        tv.edtGeradenbrz.place(relx=0.7, rely=0.42, anchor=ctk.CENTER)

        tv.lblGeraden = ctk.CTkLabel(tv.tab("Geradenbeziehungen"), text="")
        tv.lblGeraden.place(relx=0.5, rely=0.68, anchor=ctk.CENTER)

        tv.lblGeradenBeziehung= ctk.CTkLabel(tv.tab("Geradenbeziehungen"), text="")
        tv.lblGeradenBeziehung.place(relx=0.5, rely=0.78, anchor=ctk.CENTER)

        tv.lblGeradenWinkel = ctk.CTkLabel(tv.tab("Geradenbeziehungen"), text="")
        tv.lblGeradenWinkel.place(relx=0.5, rely=0.86, anchor=ctk.CENTER)

        tv.lblGeradenNormal = ctk.CTkLabel(tv.tab("Geradenbeziehungen"), text="")
        tv.lblGeradenNormal.place(relx=0.5, rely=0.94, anchor=ctk.CENTER)

    def clear(self, tab):
        tv = self.tab_view
        match tab:
            case "Vektor":
                tv.lblVektor.configure(text="")
                tv.lblVektorLength.configure(text="")
                tv.lblVektorNormal.configure(text="")
            case "Vektorbeziehungen":
                tv.lblVektoren.configure(text="")
                tv.lblVektorenNormal.configure(text="")
                tv.lblVektorenSkalar.configure(text="")
                tv.lblVektorenWinkel.configure(text="")
            case "Gerade":
                tv.lblGerade.configure(text="")
                tv.lblGeradeNormal.configure(text="")
                tv.lblGeradeSpurpunkte.configure(text="")
            case "Geradenbeziehungen":
                tv.lblGeraden.configure(text="")
                tv.lblGeradenBeziehung.configure(text="")
                tv.lblGeradenNormal.configure(text="")
                tv.lblGeradenWinkel.configure(text="")

    def btnDimensions_callback(self, option):
        tv = self.tab_view
        if option == "2":
            tv.edtVektorz.configure(state="disabled")
            tv.edtVektorenaz.configure(state="disabled")
            tv.edtVektorenbz.configure(state="disabled")
            tv.edtGeradesz.configure(state="disabled")
            tv.edtGeraderz.configure(state="disabled")
            tv.edtGeradenasz.configure(state="disabled")
            tv.edtGeradenarz.configure(state="disabled")
            tv.edtGeradenbsz.configure(state="disabled")
            tv.edtGeradenbrz.configure(state="disabled")
        else:
            tv.edtVektorz.configure(state="normal")
            tv.edtVektorenaz.configure(state="normal")
            tv.edtVektorenbz.configure(state="normal")
            tv.edtGeradesz.configure(state="normal")
            tv.edtGeraderz.configure(state="normal")
            tv.edtGeradenasz.configure(state="normal")
            tv.edtGeradenarz.configure(state="normal")
            tv.edtGeradenbsz.configure(state="normal")
            tv.edtGeradenbrz.configure(state="normal")

    def btnGithub_callback(self):
        wb.open(self.btnGithub.cget("text"))

    def btnVektor_callback(self):
        self.clear("Vektor")
        vector = []
        vector.append(self.tab_view.edtVektorx.get())
        vector.append(self.tab_view.edtVektory.get())
        if self.btnDimensions.get() == "3":
            vector.append(self.tab_view.edtVektorz.get())
        try:
            vector_obj = vector_tools.Vector(vector)
        except ValueError:
            self.tab_view.lblVektor.configure(text="wrong input")
            return
        self.tab_view.lblVektor.configure(text="Vektor: " + str(vector_obj))
        self.tab_view.lblVektorLength.configure(text="Länge: " + str(vector_obj.length()) + " LE")
        if vector_obj.zero:
            self.tab_view.lblVektorNormal.configure(text="Normalenvektor: unbestimmt")
        else:
            self.tab_view.lblVektorNormal.configure(text="Normalenvektor: " + str(vector_obj.normal_vector()))

    def btnVektoren_callback(self):
        self.clear("Vektorbeziehungen")
        a, b = [], []
        a.append(self.tab_view.edtVektorenax.get())
        b.append(self.tab_view.edtVektorenbx.get())
        a.append(self.tab_view.edtVektorenay.get())
        b.append(self.tab_view.edtVektorenby.get())
        if self.btnDimensions.get() == "3":
            a.append(self.tab_view.edtVektorenaz.get())
            b.append(self.tab_view.edtVektorenbz.get())
        try:
            ab = vector_tools.Vectors(vector_tools.Vector(a), vector_tools.Vector(b))
        except ValueError:
            self.tab_view.lblVektoren.configure(text="wrong input")
            return
        self.tab_view.lblVektoren.configure(text="Vektoren: " + str(ab))
        self.tab_view.lblVektorenSkalar.configure(text="Skalarprodukt: " + str(ab.dot_product()))
        parallel = ab.kolinear()
        if parallel:
            self.tab_view.lblVektorenWinkel.configure(text="Winkel: 0° -> kolinear")
        elif ab.orthogonal():
            self.tab_view.lblVektorenWinkel.configure(text="Winkel: 90° -> orthogonal")
        else:
            self.tab_view.lblVektorenWinkel.configure(text="Winkel: " + str(ab.small_angle()) + "°")
        normal = ab.normal_vector()
        if normal != None:
            self.tab_view.lblVektorenNormal.configure(text="Normalenvektor: " + str(normal))

    def btnGerade_callback(self):
        self.clear("Gerade")
        s, r = [], []
        s.append(self.tab_view.edtGeradesx.get())
        r.append(self.tab_view.edtGeraderx.get())
        s.append(self.tab_view.edtGeradesy.get())
        r.append(self.tab_view.edtGeradery.get())
        if self.btnDimensions.get() == "3":
            s.append(self.tab_view.edtGeradesz.get())
            r.append(self.tab_view.edtGeraderz.get())
        try:
            line = vector_tools.Line(vector_tools.Vector(s), vector_tools.Vector(r))
        except ValueError:
            self.tab_view.lblGerade.configure(text="wrong input")
            return
        self.tab_view.lblGerade.configure(text="Gerade: " + str(line))
        if len(s) == 3:
            points = []
            flaechen = ["xy", "xz", "yz"]
            for point, location in zip(line.intersections(), flaechen):
                if point != None:
                    points.append(f"S[{location}](" + "|".join(str(i) for i in point) + ")")
            self.tab_view.lblGeradeSpurpunkte.configure(text="Spurpunkte: " + ",\n".join(i for i in points))
        self.tab_view.lblGeradeNormal.configure(text="Normalenvektor: " + str(line.normal_vector()))

    def btnGeraden_callback(self):
        self.clear("Geradenbeziehungen")
        s1, r1, s2, r2 = [], [], [], []
        s1.append(self.tab_view.edtGeradenasx.get())
        r1.append(self.tab_view.edtGeradenarx.get())
        s1.append(self.tab_view.edtGeradenasy.get())
        r1.append(self.tab_view.edtGeradenary.get())
        s2.append(self.tab_view.edtGeradenbsx.get())
        r2.append(self.tab_view.edtGeradenbrx.get())
        s2.append(self.tab_view.edtGeradenbsy.get())
        r2.append(self.tab_view.edtGeradenbry.get())
        if self.btnDimensions.get() == "3":
            s1.append(self.tab_view.edtGeradenasz.get())
            r1.append(self.tab_view.edtGeradenarz.get())
            s2.append(self.tab_view.edtGeradenbsz.get())
            r2.append(self.tab_view.edtGeradenbrz.get())
        try:
            a = vector_tools.Line(vector_tools.Vector(s1), vector_tools.Vector(r1))
            b = vector_tools.Line(vector_tools.Vector(s2), vector_tools.Vector(r2))
            ab = vector_tools.Lines(a, b)
        except ValueError:
            self.tab_view.lblGeraden.configure(text="wrong input")
            return
        self.tab_view.lblGeraden.configure(text="Geraden: " + str(ab).replace("), (", "),\n("))
        result = ab.relation()
        match result[0]:
            case 0:
                relation = "Die Geraden sind identisch."
            case 1:
                relation = "Die Geraden sind parallel."
            case 2:
                relation = "Die Geraden schneiden sich im Punkt S(" + \
                            "|".join(str(i) for i in result[1]) + ")."
            case 3:
                relation = "Die Geraden sind windschief."
        self.tab_view.lblGeradenBeziehung.configure(text=relation)
        if ab.orthogonal():
            self.tab_view.lblGeradenWinkel.configure(text="Winkel: 90°")
        else:
            self.tab_view.lblGeradenWinkel.configure(text="Winkel: " + str(ab.small_angle()) + "°")
        normal = ab.normal_vector()
        if normal != None:
            self.tab_view.lblGeradenNormal.configure(text="Normalenvektor: " + str(normal))

if __name__ == "__main__":
    app = App()
    app.mainloop()