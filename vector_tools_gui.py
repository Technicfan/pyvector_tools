import customtkinter as ctk
import webbrowser as wb
import vector_tools

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # color scheme
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
        self.lbl2 = ctk.CTkLabel(self, text="MIT Licence - Copyright (c) 2024 Technicfan")
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

        tv.lblSkalar = ctk.CTkLabel(tv.tab("Vektorbeziehungen"), text="")
        tv.lblSkalar.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        tv.lblWinkel = ctk.CTkLabel(tv.tab("Vektorbeziehungen"), text="")
        tv.lblWinkel.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

        tv.lblNormal = ctk.CTkLabel(tv.tab("Vektorbeziehungen"), text="")
        tv.lblNormal.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

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

        tv.lblSpurpunkte= ctk.CTkLabel(tv.tab("Gerade"), text="")
        tv.lblSpurpunkte.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

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

        tv.lblBeziehung= ctk.CTkLabel(tv.tab("Geradenbeziehungen"), text="")
        tv.lblBeziehung.place(relx=0.5, rely=0.78, anchor=ctk.CENTER)

    def btnDimensions_callback(self, option):
        if option == "2":
            self.tab_view.edtVektorz.configure(state="disabled")
            self.tab_view.edtVektorenaz.configure(state="disabled")
            self.tab_view.edtVektorenbz.configure(state="disabled")
            self.tab_view.edtGeradesz.configure(state="disabled")
            self.tab_view.edtGeraderz.configure(state="disabled")
            self.tab_view.edtGeradenasz.configure(state="disabled")
            self.tab_view.edtGeradenarz.configure(state="disabled")
            self.tab_view.edtGeradenbsz.configure(state="disabled")
            self.tab_view.edtGeradenbrz.configure(state="disabled")
        else:
            self.tab_view.edtVektorz.configure(state="normal")
            self.tab_view.edtVektorenaz.configure(state="normal")
            self.tab_view.edtVektorenbz.configure(state="normal")
            self.tab_view.edtGeradesz.configure(state="normal")
            self.tab_view.edtGeraderz.configure(state="normal")
            self.tab_view.edtGeradenasz.configure(state="normal")
            self.tab_view.edtGeradenarz.configure(state="normal")
            self.tab_view.edtGeradenbsz.configure(state="normal")
            self.tab_view.edtGeradenbrz.configure(state="normal")

    def btnGithub_callback(self):
        wb.open(self.btnGithub.cget("text"))

    def btnVektor_callback(self):
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

    def btnVektoren_callback(self):
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
        self.tab_view.lblSkalar.configure(text="Skalarprodukt: " + str(ab.skalar_product()))
        if ab.orthogonal():
            self.tab_view.lblWinkel.configure(text="Winkel: 90° -> orthogonal")
        else:
            self.tab_view.lblWinkel.configure(text="Winkel: " + str(ab.small_angle()) + "°")
        if len(a) == 3:
            self.tab_view.lblNormal.configure(text="Normalvektor: " + str(ab.normal_vector()))
        else:
            self.tab_view.lblNormal.configure(text="")

    def btnGerade_callback(self):
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
            self.tab_view.lblSpurpunkte.configure(text="Spurpunkte: " + ",\n".join(i for i in points))
        else:
            self.tab_view.lblSpurpunkte.configure(text="")

    def btnGeraden_callback(self):
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
        self.tab_view.lblBeziehung.configure(text=relation)

if __name__ == "__main__":
    app = App()
    app.mainloop()