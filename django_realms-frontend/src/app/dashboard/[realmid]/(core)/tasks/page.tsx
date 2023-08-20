"use client"
import Tasklist from '@/components/dashboard/tasks/tasklist'
import Pageheader from '@/components/dashboard/common/pageheader'
import React from 'react';
import { useState } from 'react';

const title = 'Tasks'

function Page() {
  const [activeTab, setActiveTab] = useState('MyTasks');
  const myTabs = [
    { name: 'MyTasks', href: '#', current: true },
    { name: 'Assigned', href: '#', current: false },
    { name: 'Configure', href: '#', current: false },
 
  ];

  const actions = (
    <div className="page-header-actions">
      
      <button
        type="button"
        className="page-header-actions-button">
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

export default Page;