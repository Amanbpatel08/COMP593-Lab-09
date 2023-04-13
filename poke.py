from  tkinter import ttk
from tkinter import *
from api import get_pokemon_details
from tkinter import messagebox
window=Tk()

window.title('Pokemon Information')
window.resizable(False,False)

def get_pokemon_info():
    name=entry_name.get()
    print(name)
    if name=='':
        return
    poke_info=get_pokemon_details(name)
    if poke_info is None:
        err_msg=f'Unable to get information from the PokeAPI for {name}.'
        messagebox.showinfo(title='Error',message=err_msg,icon='error')
        return
    print()
    lbl_height_value['text']=f"{poke_info['height']} dm"
    prg_hp['value']=poke_info['stats'][0]['base_stat']
    prg_attack['value']=poke_info['stats'][1]['base_stat']
    prg_defense['value']=poke_info['stats'][2]['base_stat']


    return


frm_top=ttk.Frame(window)
frm_top.grid(row=0,column=0,padx=10,pady=10)


frm_btm_rgt=ttk.LabelFrame(window,text='Stats')
frm_btm_rgt.grid(row=1,column=1,padx=500,pady=(0,10))

frm_btm_lft=ttk.LabelFrame(window,text='Info')
frm_btm_lft.grid(row=1,column=0,sticky=N,padx=(10,0))

lbl_name=ttk.Label(frm_top,text='Pockemon Name')
lbl_name.grid(row=0,column=0,padx=10)

entry_name=ttk.Entry(frm_top)
entry_name.grid(row=0,column=1,padx=10)

button=ttk.Button(frm_top,text='Get Info',command=get_pokemon_info)
button.grid(row=0,column=2,padx=10)


lbl_height=ttk.Label(frm_btm_lft,text='Height:')
lbl_height.grid(row=0,column=0)

lbl_height_value=ttk.Label(frm_btm_lft,text='TBD')
lbl_height_value.grid(row=0,column=1)

lbl_HP=ttk.Label(frm_btm_rgt,text='HP:')
lbl_HP.grid(row=0,column=0,sticky=E)
prg_hp=ttk.Progressbar(frm_btm_rgt,orient=HORIZONTAL,length=200,maximum=300)
prg_hp.grid(row=0,column=1)

lbl_attack=ttk.Label(frm_btm_rgt,text='Attack:')
lbl_attack.grid(row=1,column=0,sticky=E)
prg_attack=ttk.Progressbar(frm_btm_rgt,orient=HORIZONTAL,length=200,maximum=300)
prg_attack.grid(row=1,column=1)

lbl_defense=ttk.Label(frm_btm_rgt,text='Defense:')
lbl_defense.grid(row=2,column=0,sticky=E)
prg_defense=ttk.Progressbar(frm_btm_rgt,orient=HORIZONTAL,length=200,maximum=300)
prg_defense.grid(row=2,column=1)

prg_hp=ttk.Progressbar(frm_btm_rgt,orient=HORIZONTAL,length=200,maximum=200)
prg_hp.grid(row=0,column=1)


window.mainloop()
