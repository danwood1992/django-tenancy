"use client"
import Tasklist from './tasklist'
import Pageheader from '../../_components/pageheader'
import React from 'react';
import { useState } from 'react';

const title = 'Tasks'

function Tasks() {
  const [activeTab, setActiveTab] = useState('MyTasks');
  const myTabs = [
    { name: 'MyTasks', href: '#', current: true },
    { name: 'Assigned', href: '#', current: false },
    { name: 'Configure', href: '#', current: false },
 
  ];

  const actions = (
    <div className="p-4 flex md:absolute md:right-0 md:top-3 md:mt-0 mr-2 ">
      
      <button
        type="button"
        className="ml-3 inline-flex items-center rounded-md bg-slate-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      >
        Add Task
      </button>
    </div>
  );
  
  return (
    <div>
      <Pageheader 
        title={title} 
        tabs={myTabs} 
        actions={actions} 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
      />
      {activeTab === 'MyTasks' && <div>My Tasks <Tasklist /></div>}
      {activeTab === 'Assigned' && <div>Billing Content</div>}
      {activeTab === 'Configure' && <div>Notifications Content</div>}

    </div>
  ); 
   
     
  
}

export default Tasks;