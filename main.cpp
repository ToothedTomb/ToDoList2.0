#include <gtkmm.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

class ToDoApp : public Gtk::Window {
public:
    ToDoApp() {
        // Window setup
        set_title("Objective Oasis - To Do List:");
        set_resizable(true);
        set_default_size(480, 455);
        set_border_width(20);

        // Menu Bar setup
        m_menubar.set_name("menubar");

        // Create File menu items
        m_new_item.set_label("New");
        m_new_item.signal_activate().connect(sigc::mem_fun(*this, &ToDoApp::on_new_task));

        m_open_item.set_label("Open");
        m_open_item.signal_activate().connect(sigc::mem_fun(*this, &ToDoApp::on_open_list));

        m_save_item.set_label("Save");
        m_save_item.signal_activate().connect(sigc::mem_fun(*this, &ToDoApp::on_save_list));

        // Create the File menu and add items
        m_file_menu.append(m_new_item);
        m_file_menu.append(m_open_item);
        m_file_menu.append(m_save_item);

        // Create the File menu item in the menu bar
        m_file_menu_item.set_label("File");
        m_file_menu_item.set_submenu(m_file_menu);
        m_menubar.append(m_file_menu_item);

        m_box.pack_start(m_menubar, Gtk::PACK_SHRINK);  // Add menu bar at the top
        m_box.pack_start(m_title_label, Gtk::PACK_SHRINK);

        // ScrolledWindow for task list to allow scrolling
        m_scrolled_window.add(m_task_listbox); // Add the ListBox to the ScrolledWindow
        m_scrolled_window.set_policy(Gtk::POLICY_AUTOMATIC, Gtk::POLICY_ALWAYS); // Automatically show scrollbars when needed
        m_box.pack_start(m_scrolled_window, Gtk::PACK_EXPAND_WIDGET);  // Add ScrolledWindow to the box

        // Entry box for task input
        m_task_entry.set_placeholder_text("Enter new task...");
        m_box.pack_start(m_task_entry, Gtk::PACK_SHRINK);

        // Button setup for adding tasks
        Gtk::Button* add_task_btn = Gtk::manage(new Gtk::Button("New Task"));
        add_task_btn->signal_clicked().connect(sigc::mem_fun(*this, &ToDoApp::on_add_task));
        m_box.pack_start(*add_task_btn, Gtk::PACK_SHRINK);

        // Window content
        add(m_box);
        show_all_children();
    }

protected:
    void on_new_task() {
        // Clear the task list and reset UI for a fresh list
        m_tasks.clear();
        m_task_listbox.foreach([this](Gtk::Widget& widget) {
            m_task_listbox.remove(widget); // Remove all tasks from the listbox
        });
    }

    void on_open_list() {
        Gtk::FileChooserDialog dialog("Open Tasks File", Gtk::FILE_CHOOSER_ACTION_OPEN);
        dialog.add_button("_Cancel", Gtk::RESPONSE_CANCEL);
        dialog.add_button("_Open", Gtk::RESPONSE_OK);

        // Show only text files
        Glib::RefPtr<Gtk::FileFilter> filter = Gtk::FileFilter::create();
        filter->set_name("Text Files");
        filter->add_mime_type("text/plain");
        dialog.add_filter(filter);

        if (dialog.run() == Gtk::RESPONSE_OK) {
            std::string filename = dialog.get_filename();
            load_tasks(filename);
        }
    }

    void on_save_list() {
        Gtk::FileChooserDialog dialog("Save Tasks File", Gtk::FILE_CHOOSER_ACTION_SAVE);
        dialog.add_button("_Cancel", Gtk::RESPONSE_CANCEL);
        dialog.add_button("_Save", Gtk::RESPONSE_OK);

        // Show only text files
        Glib::RefPtr<Gtk::FileFilter> filter = Gtk::FileFilter::create();
        filter->set_name("Text Files");
        filter->add_mime_type("text/plain");
        dialog.add_filter(filter);

        if (dialog.run() == Gtk::RESPONSE_OK) {
            std::string filename = dialog.get_filename();
            save_tasks(filename);
        }
    }

    void load_tasks(const std::string& filename) {
        std::ifstream file(filename);
        if (file) {
            std::string line;
            std::string task;

            // Clear existing tasks from the listbox
            m_task_listbox.foreach([this](Gtk::Widget& widget) {
                m_task_listbox.remove(widget); // Remove each widget from the listbox
            });

            m_tasks.clear(); // Clear the task vector

            // Read tasks from the file and add them to the listbox
            while (std::getline(file, line)) {
                add_task_to_listbox(line);
            }
        } else {
            std::cerr << "Failed to open file for reading." << std::endl;
        }
    }

    void save_tasks(const std::string& filename) {
        std::ofstream file(filename);
        if (file) {
            for (const auto& task : m_tasks) {
                file << task << std::endl;  // Save each task to the file
            }
        } else {
            std::cerr << "Failed to open file for writing." << std::endl;
        }
    }

    void on_add_task() {
        std::string task_text = m_task_entry.get_text();
        if (!task_text.empty()) {
            add_task_to_listbox(task_text);
        }
    }

    void add_task_to_listbox(const std::string& task) {
        // Add task to the listbox
        Gtk::Box* task_box = Gtk::manage(new Gtk::Box(Gtk::ORIENTATION_HORIZONTAL));
        Gtk::Label* task_label = Gtk::manage(new Gtk::Label(task));
        Gtk::Button* delete_button = Gtk::manage(new Gtk::Button("Delete"));

        // Task deletion callback
        delete_button->signal_clicked().connect([this, task_box, task_label, task]() {
            // Remove task from the vector
            auto it = std::find(m_tasks.begin(), m_tasks.end(), task);
            if (it != m_tasks.end()) {
                m_tasks.erase(it); // Erase the task from the vector
            }

            // Find and remove the task row from the listbox
            for (auto row : m_task_listbox.get_children()) {
                auto list_row = dynamic_cast<Gtk::ListBoxRow*>(row);
                if (list_row) {
                    auto box = dynamic_cast<Gtk::Box*>(list_row->get_children()[0]);
                    if (box) {
                        auto label = dynamic_cast<Gtk::Label*>(box->get_children()[0]);
                        if (label && label->get_text() == task_label->get_text()) {
                            m_task_listbox.remove(*list_row); // Remove the row from the listbox
                            break; // Stop iterating after removing the row
                        }
                    }
                }
            }
        });

    task_box->pack_start(*task_label, Gtk::PACK_EXPAND_WIDGET);
    task_box->pack_start(*delete_button, Gtk::PACK_SHRINK);

    Gtk::ListBoxRow* row = Gtk::manage(new Gtk::ListBoxRow());
    row->add(*task_box);

    m_task_listbox.append(*row);
    m_task_listbox.show_all();

    m_tasks.push_back(task); // Store task in vector
}

private:
    Gtk::Box m_box{Gtk::ORIENTATION_VERTICAL};
    Gtk::MenuBar m_menubar;
    Gtk::Menu m_file_menu;
    Gtk::MenuItem m_file_menu_item, m_new_item, m_open_item, m_save_item;
    Gtk::Label m_title_label;
    Gtk::ListBox m_task_listbox;
    Gtk::Entry m_task_entry;
    Gtk::ScrolledWindow m_scrolled_window; // Scrollable window for task list
    std::vector<std::string> m_tasks; // Vector of tasks
};

int main(int argc, char* argv[]) {
    auto app = Gtk::Application::create(argc, argv, "com.example.objective_oasis");
    ToDoApp window;
    return app->run(window);
}
